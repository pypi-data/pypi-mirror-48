# coding: utf-8

import argparse
import asyncio
import logging
import sys
import os
import threading
import datetime, time
import subprocess
import signal
from aiortcdc import RTCPeerConnection, RTCSessionDescription

#from os import path
#sys.path.append(path.dirname(path.abspath(__file__)) + "/../")

from onatlib.signaling_share_ws import create_signaling, add_signaling_arguments
import websocket
import traceback
import socket
import random
import string

sctp_transport_established = False
force_exited = False

remote_stdout_connected = False
remote_stdin_connected = False
sender_fifo_q = asyncio.Queue()
receiver_fifo_q = asyncio.Queue()
signaling = None
client_address = None
send_ws = None
sub_channel_sig = None
is_remote_node_exists_on_my_send_room = False

is_received_client_disconnect_request = False

server_send = None
server_rcv = None

cur_recv_clientsock = None
file_transfer_mode = False
file_transfer_phase = 0

next_sender_handler_id = 0
queue_lock = threading.Lock()

# except header data
sender_recv_bytes_from_client = 0
sender_client_eof_or_disconnected = False

def get_random_ID(length):
    dat = string.digits + string.digits + string.digits + \
            string.ascii_lowercase + string.ascii_uppercase

    return ''.join([random.choice(dat) for times in range(length)])

async def consume_signaling(pc, signaling):
    global force_exited
    global remote_stdout_connected
    global remote_stin_connected

    while True:
        try:
            obj = await signaling.receive()

            if isinstance(obj, RTCSessionDescription):
                await pc.setRemoteDescription(obj)

                if obj.type == 'offer':
                    # send answer
                    await pc.setLocalDescription(await pc.createAnswer())
                    await signaling.send(pc.localDescription)
            elif isinstance(obj, str) and force_exited == False:
                #print("string recievd: " + obj, file=sys.stderr)
                continue
            else:
                print('Exiting', file=sys.stderr)
                break
        except:
            traceback.print_exc()


async def run_answer(pc, signaling):
    await signaling.connect()

    @pc.on('datachannel')
    def on_datachannel(channel):
        global sctp_transport_established
        start = time.time()
        #octets = 0
        sctp_transport_established = True
        print("datachannel established")
        sys.stdout.flush()
        is_checked_filetransfer = False
        fp = None
        file_transfer_filename = None

        @channel.on('message')
        async def on_message(message):
            global file_transfer_phase
            global file_transfer_mode
            global receiver_fifo_q
            global queue_lock
            global sender_recv_bytes_from_client
            nonlocal is_checked_filetransfer
            nonlocal fp
            nonlocal file_transfer_filename

            print("message event fired", file=sys.stderr)
            print("message received from datachannel: " + str(len(message)), file=sys.stderr)

            if is_checked_filetransfer == False:
                decoded_str = None
                if message != None and len(message) == 2:
                    try:
                        decoded_str = message.decode()
                    except:
                        is_checked_filetransfer = True

                    if decoded_str != None and decoded_str == "sf":
                        #await receiver_fifo_q.put(message)
                        file_transfer_phase = 1
                        return
                    else:
                        is_checked_filetransfer = True

                if file_transfer_phase == 1:
                    #await receiver_fifo_q.put(message)
                    try:
                        decoded_str = message.decode()
                        print("filename bytes: " + decoded_str)
                        file_transfer_phase = 2
                        return
                    except:
                        traceback.print_exc()

                if file_transfer_phase == 2:
                    try:
                        print(message.decode())
                        file_transfer_filename = message.decode()
                        fp = open(file_transfer_filename, "wb")
                    except:
                        traceback.print_exc()
                    file_transfer_mode = True
                    is_checked_filetransfer = True
                    file_transfer_phase = 0
                    return

            if file_transfer_mode == True:
                try:
                    if len(message) > 0:
                        if len(message) == 8 and message.decode() == "finished":
                            fp.flush()
                            fp.close()
                            fp = None
                            is_checked_filetransfer = False
                            file_transfer_phase = 0
                            file_transfer_mode = False
                            return
                        else:
                            print("write " + str(len(message)) + " bytes to " + file_transfer_filename)
                            fp.write(message)
                except:
                    traceback.print_exc()
            else:
                try:
                    if len(message) > 0:
                        if len(message) == 8 and message.decode() == "finished":
                            is_checked_filetransfer = False
                            file_transfer_phase = 0
                            file_transfer_mode = False
                            print("put data to queue: " + str(len(message)))
                            queue_lock.acquire()
                            await receiver_fifo_q.put(message)
                            return
                        else:
                            print("put data to queue: " + str(len(message)))
                            queue_lock.acquire()
                            await receiver_fifo_q.put(message)
                except:
                    traceback.print_exc()
                    ws_sender_send_wrapper("receiver_disconnected")
                    # say goodbye
                    #await signaling.send(Nne)
                finally:
                    queue_lock.release()

    await signaling.send("join")
    await consume_signaling(pc, signaling)

async def run_offer(pc, signaling):
    while True:
        try:
            await signaling.connect()
            await signaling.send("joined_members")

            cur_num_str = await signaling.receive()
            print("cur_num_str: " + cur_num_str, file=sys.stderr)
            if "ignoalable error" in cur_num_str:
                pass
            elif cur_num_str != "0":
                await asyncio.sleep(2)
                break
            else:
                await signaling.close()

            print("wait join of receiver", file=sys.stderr)
            await asyncio.sleep(1)
        except:
            traceback.print_exc()
    await signaling.connect()
    await signaling.send("join")

    channel_sender = pc.createDataChannel('filexfer')

    async def send_data_inner():
        nonlocal channel_sender
        global sctp_transport_established
        global sender_fifo_q
        global remote_stdout_connected
        global file_transfer_mode
        global queue_lock
        global next_sender_handler_id
        global sender_recv_bytes_from_client
        global sender_client_eof_or_disconnected

        # this line is needed?
        asyncio.set_event_loop(asyncio.new_event_loop())
        sent_bytes = 0

        while True:
            sctp_transport_established = True
            while remote_stdout_connected == False and file_transfer_mode == False:
                print("wait remote_stdout_connected", file=sys.stderr)
                await asyncio.sleep(1)

            print("start waiting buffer state is OK", file=sys.stderr)
            while channel_sender.bufferedAmount > channel_sender.bufferedAmountLowThreshold:
                #print("buffer info of channel: " + str(channel_sender.bufferedAmount) + " > " + str( channel_sender.bufferedAmountLowThreshold))
                await asyncio.sleep(1)

            print("start sending roop", file=sys.stderr)
            while channel_sender.bufferedAmount <= channel_sender.bufferedAmountLowThreshold:
                try:
                    data = None
                    is_empty = False
                    try:
                        queue_lock.acquire()
                        is_empty = sender_fifo_q.empty()
                        print("queue is empty? at send_data_inner: " + str(is_empty), file=sys.stderr)
                        if is_empty != True:
                            #print("queue object id" + str(id(sender_fifo_q)))
                            data = await sender_fifo_q.get()
                    except:
                        traceback.print_exc()
                    finally:
                        queue_lock.release()

                    if is_empty == True:
                         await asyncio.sleep(1)
                         continue

                    if data:
                        # if not current client puted data, do ignore
                        if data[0] != (next_sender_handler_id - 1):
                            continue

                        sent_bytes += len(data[1])
                        print("send_data: " + str(len(data[1])))
                        sys.stdout.flush()
                        channel_sender.send(data[1])

                        # sender_server_handler received data from client are all sent
                        if sent_bytes == sender_recv_bytes_from_client and sender_client_eof_or_disconnected:
                            print("notify end of transfer")
                            channel_sender.send("finished".encode())
                            file_transfer_mode = False
                            sent_bytes = 0
                            sender_recv_bytes_from_client = 0
                            sender_client_eof_or_disconnected = False
                            remote_stdout_connected = False
                            queue_lock.acquire()
                            sender_fifo_q = asyncio.Queue()
                            queue_lock.release()

                    await asyncio.sleep(0.01)
                except:
                    traceback.print_exc()

    async def send_data():
        print("datachannel established")
        sys.stdout.flush()
        await send_data_inner()

    #channel_sender.on('bufferedamountlow', send_data)
    channel_sender.on('open', send_data)

    # send offer
    await pc.setLocalDescription(await pc.createOffer())
    await signaling.send(pc.localDescription)

    await consume_signaling(pc, signaling)

async def ice_establishment_state():
    global force_exited
    while(sctp_transport_established == False and "failed" not in pc.iceConnectionState):
        print("ice_establishment_state: " + pc.iceConnectionState, file=sys.stderr)
        await asyncio.sleep(1)
    if sctp_transport_established == False:
        print("hole punching to remote machine failed.")
        force_exited = True
        try:
            loop.stop()
            loop.close()
        except:
            pass
        print("exit.")

# app level websocket sending should anytime use this (except join message)
def ws_sender_send_wrapper(msg):
    if send_ws:
        send_ws.send(sub_channel_sig + "_chsig:" + msg)

# app level websocket sending should anytime use this
def ws_sender_recv_wrapper():
    if send_ws:
        return send_ws.recv()
    else:
        return None

def work_as_parent():
    pass

# async def clear_queue(queue_obj):
#     #global queue_lock
#
#     print("call clear_queue")
#     #queue_lock.acquire()
#     while queue_obj.empty() == False:
#         #queue_obj.get()
#         try:
#             queue_obj.get_nowait()
#         except:
#             traceback.print_exc()
#
#         qsize = await queue_obj.qsize()
#         print(qsize)
#         await asyncio.sleep(0.01)
#
#     #queue_lock.release()

async def sender_server_handler(reader, writer):
    global sender_fifo_q
    global file_transfer_mode
    global is_checked_filetransfer
    global next_sender_handler_id
    global queue_lock
    global sender_client_eof_or_disconnected
    global sender_recv_bytes_from_client

    print('Local server writer port waiting for client connections...')

    byte_buf = b''
    is_checked_filetransfer = False
    rcvmsg = None

    # reset not to send old client wrote data
    queue_lock.acquire()
    sender_fifo_q = asyncio.Queue()
    #await clear_queue(sender_fifo_q)
    queue_lock.release()

    this_sender_handler_id = next_sender_handler_id
    this_sender_handler_id_str = str(this_sender_handler_id)
    next_sender_handler_id += 1
    try:
        print("new client connected.")
        print("wake up new sender_server_handler [" + str(this_sender_handler_id_str)  + "]")
        # wait remote server is connected with some program
        head_2byte = b''
        while remote_stdout_connected == False and file_transfer_mode == False:
            print("wait remote_stdout_connected", file=sys.stderr)
            if is_checked_filetransfer == False:
                rcvmsg = await reader.read(1)
                #print(rcvmsg)
                head_2byte = b''.join([head_2byte, rcvmsg])
                try:
                    if len(head_2byte) == 1:
                        if head_2byte.decode() == "s":
                            #print("first byte is *s*")
                            #sys.stdout.flush()
                            continue
                        else:
                            #print("not s")
                            #sys.stdout.flush()
                            is_checked_filetransfer = True
                except:
                    pass

                decoded_str = None
                if rcvmsg != None and len(head_2byte) == 2:
                    try:
                        decoded_str = head_2byte.decode()
                    except:
                        pass
                    if decoded_str == "sf":
                        try:
                            print("file transfer mode [" + this_sender_handler_id_str + "]")
                            queue_lock.acquire()
                            await sender_fifo_q.put([this_sender_handler_id, head_2byte])
                            rcvmsg = await reader.read(3)
                            filename_bytes = int(rcvmsg.decode())
                            await sender_fifo_q.put([this_sender_handler_id, rcvmsg])
                            print(filename_bytes)
                            rcvmsg = await reader.read(filename_bytes)
                            print(rcvmsg.decode())
                            await sender_fifo_q.put([this_sender_handler_id, rcvmsg])
                            file_transfer_mode = True
                            is_checked_filetransfer = True
                            sender_recv_bytes_from_client += 2 + 3 + filename_bytes
                        except:
                            pass
                        finally:
                            queue_lock.release()
                        continue
                    else:
                        sender_recv_bytes_from_client += len(head_2byte)
                        byte_buf = b''.join([byte_buf, head_2byte])
                        is_checked_filetransfer = True
                else:
                    sender_recv_bytes_from_client += len(head_2byte)
                    byte_buf = b''.join([byte_buf, head_2byte])
                    is_checked_filetransfer = True

            await asyncio.sleep(1)

        while True:
            # if flag backed to False, end this handler because it means receiver side client disconnected
            if remote_stdout_connected == False and file_transfer_mode == False:
                # clear bufferd data
                # if sender_fifo_q.empty() == False:
                #     print("reset sender_fifo_q because it is not empty")
                #     sender_fifo_q = asyncio.Queue()
                #return
                queue_lock.acquire()
                sender_fifo_q = asyncio.Queue()
                #await clear_queue(sender_fifo_q)
                queue_lock.release()
                await asyncio.sleep(3)
            try:
                rcvmsg = await reader.read(5120)
                sender_recv_bytes_from_client += len(rcvmsg)

                byte_buf = b''.join([byte_buf, rcvmsg])
                print("received message from client[" + this_sender_handler_id_str + "]", file=sys.stderr)
                print(len(rcvmsg), file=sys.stderr)

                if args.no_buffering != True:
                    # block sends until bufferd data amount is gleater than 100KB
                    if(len(byte_buf) <= 1024 * 512) and (rcvmsg != None and len(rcvmsg) > 0): #1MB
                        print("current bufferd byteds: " + str(len(byte_buf)), file=sys.stderr)
                        await asyncio.sleep(0.01)
                        continue
            except:
                traceback.print_exc()

            #print("len of recvmsg:" + str(len(recvmsg)))
            if rcvmsg == None or len(rcvmsg) == 0:
                #print(rcvmsg)
                if len(byte_buf) > 0:
                    queue_lock.acquire()
                    await sender_fifo_q.put([this_sender_handler_id, byte_buf])
                    queue_lock.release()
                    byte_buf = b''
                sender_client_eof_or_disconnected = True
                print("reached EOF or client disconnection [" + this_sender_handler_id_str + "]")
                return
            else:
                print("put bufferd bytes [" + this_sender_handler_id_str + "]: " + str(len(byte_buf)), file=sys.stderr)
                queue_lock.acquire()
                await sender_fifo_q.put([this_sender_handler_id, byte_buf])
                queue_lock.release()
                byte_buf = b''
            await asyncio.sleep(0.01)
    except:
        traceback.print_exc()

async def sender_server():
    global server_send

    try:
        server_send = await asyncio.start_server(
            sender_server_handler, '127.0.0.1', args.send_stream_port)
    except:
        traceback.print_exc()

    async with server_send:
        await server_send.serve_forever()


async def receiver_server_handler(clientsock):
    global receiver_fifo_q
    global is_remote_node_exists_on_my_send_room
    global is_received_client_disconnect_request
    global send_ws
    global sub_channel_sig
    global cur_recv_clientsock
    global next_sender_handler_id

    this_sender_handler_id = next_sender_handler_id
    this_sender_handler_id_str = str(this_sender_handler_id)
    next_sender_handler_id += 1

    print("new receiver server_handler wake up [" + this_sender_handler_id_str + "]")
    # clear queue for avoiding read left data on queue
    queue_lock.acquire()
    receiver_fifo_q = asyncio.Queue()
    #await clear_queue(receiver_fifo_q)
    queue_lock.release()
    is_already_send_receiver_connected = False

    # try:
    #     if send_ws:
    #         send_ws.close()
    #         send_ws = None
    # except:
    #     traceback.print_exc()

    while True:
        try:
            while is_remote_node_exists_on_my_send_room == False:
                send_ws = websocket.create_connection(
                    ws_protcol_str + "://" + args.signaling_host + ":" + str(args.signaling_port) + "/")
                sub_channel_sig = args.gid + "rtos"
                ws_sender_send_wrapper("joined_members_sub")

                message = ws_sender_recv_wrapper()
                #print("response of joined_members_sub: " + message)
                splited = message.split(":")
                member_num = int(splited[1])
                if member_num >= 1:
                    is_remote_node_exists_on_my_send_room = True
                    ws_sender_send_wrapper("join")
                    #ws_sender_send_wrapper("receiver_connected")
                    #print("new client connected")
                else:
                    send_ws.close()
                    send_ws = None
                    await asyncio.sleep(3)

            if is_already_send_receiver_connected == False:
                ws_sender_send_wrapper("receiver_connected")
                is_already_send_receiver_connected = True

            data = None
            is_empty = False
            try:
                queue_lock.acquire()
                is_empty = receiver_fifo_q.empty()
                print("queue is empty? at receiver_server_handler [" + this_sender_handler_id_str + "]: " + str(is_empty), file=sys.stderr)
                if is_empty != True:
                    data = await receiver_fifo_q.get()
                    print("got get data from queue[" + this_sender_handler_id_str + "]", file=sys.stderr)
            except:
                traceback.print_exc()
                #break
                return
            finally:
                queue_lock.release()

            if is_empty == False:
                await asyncio.sleep(1)

            if data:
                print("send_data [" + this_sender_handler_id_str + "]: " + str(len(data)))
                if len(data) == 8: # maybe "finished message"
                    decoded_str = ""
                    try:
                        decoded_str = data.decode()
                    except:
                        pass

                    if decoded_str == "finished":
                        clientsock.close()
                        return

                clientsock.sendall(data)
                #clientsock.flush()
                #print("client is_closing:" + str(writer.transport.is_closing()))

                # if len(data) == 8: # maybe "finished message"
                #     decoded_str = None
                #     try:
                #         decoded_str = data.decode()
                #     except:
                #         continue
                #         #traceback.print_exc()
                #
                #     if decoded_str == "finished":
                #         return
            await asyncio.sleep(0.01)
        except:
            print(type(clientsock))
            print(clientsock)
            traceback.print_exc()
            print("client disconnected.[" + this_sender_handler_id_str + "]")
            # try:
            #     clientsock.cloe()
            # except:
            #     traceback.print_exc()
            # cur_recv_clientsock = None
            #ws_sender_send_wrapper("receiver_disconnected")
            #break
            #return

# use global variable
def async_coloutin_loop_run__for_sock_th(clientsock):
    loop = asyncio.new_event_loop()
    loop.run_until_complete(receiver_server_handler(clientsock))

def receiver_server():
    global server_rcv
    global cur_recv_clientsock

    server_rcv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_rcv.bind(("127.0.0.1", args.recv_stream_port))
    server_rcv.listen()

    while True:
        if cur_recv_clientsock == None:
            print('Local server reader port waiting for client connections...')
        clientsock, client_address = server_rcv.accept()
        print("new client accepted.")

        # though there is already communicating client, accept new client
        if cur_recv_clientsock == None:
            print("new client connected.")
        else:
            print("already client exist.")
            print("disconnect old connection.")
            try:
                cur_recv_clientsock.close()
            except:
                traceback.print_exc()
        cur_recv_clientsock = clientsock

        thread = threading.Thread(target=async_coloutin_loop_run__for_sock_th, daemon=True, args=([clientsock]))
        thread.start()


async def send_keep_alive():
    while True:
        ws_sender_send_wrapper("keepalive")
        #time.sleep(5)
        await asyncio.sleep(5)

def setup_ws_sub_sender_for_sender_server():
    global send_ws
    global sub_channel_sig
    send_ws = websocket.create_connection(ws_protcol_str +  "://" + args.signaling_host + ":" + str(args.signaling_port) + "/")
    print("sender app level ws (2) opend")
    sub_channel_sig = args.gid + "stor"
    ws_sender_send_wrapper("join")

def ws_sub_receiver():
    def on_message(ws, message):
        global remote_stdout_connected
        global remote_stdin_connected
        global done_reading
        global is_received_client_disconnect_request

        #print(message,  file=sys.stderr)
        print("called on_message", file=sys.stderr)
        #print(message)

        if "receiver_connected" in message:
            if remote_stdout_connected == False:
                print("receiver_connected")
            #print(fifo_q.getbuffer().nbytes)
            remote_stdout_connected = True
            # if fifo_q.getbuffer().nbytes != 0:
            #     send_data()
        elif "receiver_disconnected" in message:
            remote_stdout_connected = False
            done_reading = False
        elif "sender_connected" in message:
            remote_stdin_connected = True
        elif "sender_disconnected" in message:
            print("sender_disconnected")
            remote_stdin_connected = False
            is_received_client_disconnect_request = True
            # if clientsock:
            #     time.sleep(5)
            #     print("disconnect clientsock")
            #     clientsock.close()
            #     clientsock = None

    def on_error(ws, error):
        print(error)

    def on_close(ws):
        print("### closed ###")

    def on_open(ws):
        print("app level ws (1) opend")
        try:
            if args.role == 'send':
                ws.send(args.gid + "rtos_chsig:join")
            else:
                ws.send(args.gid + "stor_chsig:join")
        except:
            traceback.print_exc()

    ws = websocket.WebSocketApp(ws_protcol_str + "://" + args.signaling_host + ":" + str(args.signaling_port) + "/",
                                    on_message=on_message,
                                    on_error=on_error,
                                    on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()

async def parallel_by_gather():
    # execute by parallel
    def notify(order):
        print(order + " has just finished.")

    cors = None
    if args.role == 'send':
        cors = [run_offer(pc, signaling), sender_server(), ice_establishment_state(), send_keep_alive()]
    else:
        cors = [run_answer(pc, signaling), ice_establishment_state(), send_keep_alive()]
    await asyncio.gather(*cors)
    return

def stdout_piper_th(role, proc):
    fileno = sys.stdout.fileno()
    with open(fileno, "wb", closefd=False) as stdout_fd:
        while not proc.poll():
            stdout_data = proc.stdout.readline()
            if stdout_data:
                #sys.stdout.write(stdoutdata.decode())
                #stdout_fd.write(stdout_data)
                stdout_fd.write(b''.join([role.encode(), ": ".encode(), stdout_data]))
                stdout_fd.flush()
            else:
                break

def stderr_piper_th(role, proc):
    fileno = sys.stderr.fileno()
    with open(fileno, "wb", closefd=False) as stderr_fd:
        while not proc.poll():
            stderr_data = proc.stderr.readline()
            if stderr_data:
                #sys.stderr.write(stderr_data.decode())
                stderr_fd.write(b''.join([role.encode(), ": ".encode(), stderr_data]))
                stderr_fd.flush()
            else:
                break

def stdout_stderr_flusher_th(interval_sec):
    while True:
        sys.stdout.flush()
        sys.stderr.flush()
        time.sleep(interval_sec)

def get_relative_this_script_path():
    if os.name == 'nt':
        return __file__
    else:
        return os.getcwd() + "/" + __file__

def keyboard_interrupt_hundler():
    if args.hierarchy == "parent":
        print("Ctrl-C keyboard interrupt received.")
        sys.stdout.flush()

        print("exit parent proc.")
        if os.name == 'nt':
            os.Kill(sender_proc.pid, signal.CTRL_C_EVENT)
            os.Kill(receiver_proc.pid, signal.CTRL_C_EVENT)
        else:
            os.Kill(sender_proc.pid, signal.SIGINT)
            os.Kill(receiver_proc.pid, signal.SIGINT)
        time.sleep(1)
    else:
        if args.role == "send":
            print("exit send proc (child).")
        else:
            print("exit recv proc (child).")

    sys.stdout.flush()
    sys.stderr.flush()
    sys.exit(0)

def get_unixtime_microsec_part():
    cur = datetime.datetime.now()
    return cur.microsecond

loop = None
pc = None
signaling = None
colo = None
sender_proc = None
receiver_proc = None
args = None
ws_protcol_str = "ws"

def main():
    global loop
    global pc
    global signaling
    global colo
    global sender_proc
    global receiver_proc
    global args
    global ws_protcol_str

    parser = argparse.ArgumentParser(description='Data channel file transfer')
    parser.add_argument('gid', default="", help="unique ID which should be shared by two users of p2p transport (if not specified, this program generate appropriate one)")
    parser.add_argument('--hierarchy', default="parent", choices=['parent', 'child'])
    parser.add_argument('--role', choices=['send', 'receive'])
    parser.add_argument('--name', choices=['tom', 'bob'])
    parser.add_argument('--verbose', '-v', action='count')
    parser.add_argument('--no-buffering', action='store_true')
    parser.add_argument('--send-stream-port', default=10100, type=int,
                        help='This local server make datachannel stream readable at this port')
    parser.add_argument('--recv-stream-port', default=10200, type=int,
                        help='This local server make datachannel stream readable at this port')
    parser.add_argument('--slide-stream-ports',
                        help='When you exec two process on same host, other side process should change streaming port', action='store_true')
    add_signaling_arguments(parser)
    args = parser.parse_args()

    # set seed from microsecond part of unixtime
    random.seed(get_unixtime_microsec_part())

    if args.gid == "please_gen":
        args.gid = get_random_ID(10)
        print("generated unique ID " + args.gid + ". you should share this with the other side user.")
        sys.exit(0)

    if len(args.gid) < 10:
        print("gid should have length at least 10 characters. I suggest use " + get_random_ID(10))
        #print("gid should have length at least 10 characters.")
        sys.exit(0)

    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)
    #websocket.enableTrace(True)

    if args.secure_signaling == True:
        ws_protcol_str = "wss"

    # register ctrl-c signal handler
    # if os.name == 'nt':
    #     signal.signal(signal.CTRL_C_EVENT, keyboard_interrupt_hundler)
    # else:
    #     signal.signal(signal.SIGINT, keyboard_interrupt_hundler)

    if args.hierarchy == 'parent':
        try:
            if args.name != "tom" and args.name != "bob":
                print("please pass --name argument. accebtable value is \\tom\\ or \\bob\\, which neeed different between communicate users (2users)")
                sys.exit(0)

            sender_cmd_args_list = []
            receiver_cmd_args_list = []
            #print(get_relative_this_script_path())
            # sender_cmd_args_list.append("python")
            # receiver_cmd_args_list.append("python")
            # sender_cmd_args_list.append("--version")
            # receiver_cmd_args_list.append("--version")
            # sender_cmd_args_list.append("cd")
            # receiver_cmd_args_list.append("cd")
            # python_path = ""
            # if os.name != "nt":
                # cmd = ['which', 'python']
                # out = subprocess.run(cmd, stdout=subprocess.PIPE)
                # python_path = out.stdout.decode()[0:-1]
                # print(python_path)
                # print("hoge")

            # if python_path == "":
            sender_cmd_args_list.append("python")
            receiver_cmd_args_list.append("python")
            # else:
            #     sender_cmd_args_list.append(python_path)
            #     receiver_cmd_args_list.append(python_path)

            sender_cmd_args_list.append(get_relative_this_script_path())
            receiver_cmd_args_list.append(get_relative_this_script_path())
            sender_cmd_args_list.append("--signaling")
            receiver_cmd_args_list.append("--signaling")
            sender_cmd_args_list.append("share-websocket")
            receiver_cmd_args_list.append("share-websocket")
            sender_cmd_args_list.append("--signaling-host")
            receiver_cmd_args_list.append("--signaling-host")
            sender_cmd_args_list.append(args.signaling_host)
            receiver_cmd_args_list.append(args.signaling_host)
            sender_cmd_args_list.append("--signaling-port")
            receiver_cmd_args_list.append("--signaling-port")
            sender_cmd_args_list.append(args.signaling_port)
            receiver_cmd_args_list.append(args.signaling_port)
            sender_cmd_args_list.append("--role")
            receiver_cmd_args_list.append("--role")
            sender_cmd_args_list.append("send")
            receiver_cmd_args_list.append("receive")
            if args.secure_signaling:
                sender_cmd_args_list.append("--secure-signaling")
                receiver_cmd_args_list.append("--secure-signaling")
            if args.slide_stream_ports:
                sender_cmd_args_list.append("--send-stream-port")
                receiver_cmd_args_list.append("--recv-stream-port")
                sender_cmd_args_list.append("10101")
                receiver_cmd_args_list.append("10201")
            if args.no_buffering:
                sender_cmd_args_list.append("--no-buffering")
                receiver_cmd_args_list.append("--no-buffering")
            if args.verbose:
                sender_cmd_args_list.append("-v")
                receiver_cmd_args_list.append("-v")
            sender_cmd_args_list.append("--hierarchy")
            receiver_cmd_args_list.append("--hierarchy")
            sender_cmd_args_list.append("child")
            receiver_cmd_args_list.append("child")
            if(args.name == "tom"):
                sender_cmd_args_list.append(args.gid + "conn1")
                receiver_cmd_args_list.append(args.gid + "conn2")
            else:
                sender_cmd_args_list.append(args.gid + "conn2")
                receiver_cmd_args_list.append(args.gid + "conn1")

            #if os.name != "nt":
            sender_cmd_args_list = " ".join(sender_cmd_args_list)
            receiver_cmd_args_list = " ".join(receiver_cmd_args_list)

            #print(sender_cmd_args_list)

            sender_proc = subprocess.Popen(sender_cmd_args_list, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            sender_stdout_piper_th = threading.Thread(target=stdout_piper_th, daemon=True, args=(["sender_proc", sender_proc]))
            sender_stdout_piper_th.start()
            sender_stderr_piper_th = threading.Thread(target=stderr_piper_th, daemon=True, args=(["sender_proc", sender_proc]))
            sender_stderr_piper_th.start()

            receiver_proc = subprocess.Popen(receiver_cmd_args_list, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            receiver_stdout_piper_th = threading.Thread(target=stdout_piper_th, daemon=True, args=(["recv_proc", receiver_proc]))
            receiver_stdout_piper_th.start()
            receiver_stderr_piper_th = threading.Thread(target=stderr_piper_th, daemon=True, args=(["recv_proc", receiver_proc]))
            receiver_stderr_piper_th.start()

            receiver_proc.wait()
        except KeyboardInterrupt:
            keyboard_interrupt_hundler()
    else: #child
        signaling = create_signaling(args)
        pc = RTCPeerConnection()

        # this feature inner syori is nazo, so not use event loop
        ws_sub_recv_th = threading.Thread(target=ws_sub_receiver, daemon=True)
        ws_sub_recv_th.start()

        flusher_th = threading.Thread(target=stdout_stderr_flusher_th, daemon=True, args=([1]))
        flusher_th.start()

        if args.role == 'send':
            setup_ws_sub_sender_for_sender_server()
            print("This local server is waiting connect request for sending your stream data to remote at " + str(args.send_stream_port) + " port.")
        elif args.role == 'receive':
            print("This local server is waiting connect request for passing stream data from remote to you at " + str(args.recv_stream_port) + " port.")
            receiver_th = threading.Thread(target=receiver_server, daemon=True)
            receiver_th.start()
        else:
            print("please pass --role {send|receive} option")

        try:
            # run event loop
            loop = asyncio.get_event_loop()
            # if os.name == 'nt':
            #     loop = asyncio.ProactorEventLoop()
            # else:
            #     loop = asyncio.get_event_loop()
            #loop.run_until_complete(coro)
            loop.run_until_complete(parallel_by_gather())
        except KeyboardInterrupt:
            #traceback.print_exc()
            keyboard_interrupt_hundler()
        finally:
            #fp.close()
            loop.run_until_complete(pc.close())
            loop.run_until_complete(signaling.close())

if __name__ == '__main__':
    main()
