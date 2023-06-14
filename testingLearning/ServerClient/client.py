# import socket

# # 접속 정보 설정
# SERVER_IP = '110.76.69.91'
# SERVER_PORT = 5050
# SIZE = 1024
# SERVER_ADDR = (SERVER_IP, SERVER_PORT)

# # 클라이언트 소켓 설정
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
#     client_socket.connect(SERVER_ADDR)  # 서버에 접속\
#     send_msg = input('your messege: ')
#     client_socket.send(send_msg.encode())  # 서버에 메시지 전송
#     msg = client_socket.recv(SIZE)  # 서버로부터 응답받은 메시지 반환
#     print("resp from server : {}".format(msg.decode()))  # 서버로부터 응답받은 메시지 출력

import socket
import threading
import time
from queue import Queue

# 접속 정보 설정
SERVER_IP = '110.76.69.91'
SERVER_PORT = 5050
SIZE = 1024
SERVER_ADDR = (SERVER_IP, SERVER_PORT)

def myin(queue):
    print('myin')
    while True:
        n = input()
        print('input took')
        if "OUT" in n: 
            # queue.put(None)
            break
        queue.put(n)
    print('myin end')

def send(queue, ended, client_socket:socket.socket):
    print('send')
    while True:
        _in = queue.get()
        print('got input, ', _in)
        if _in is None:
            # ended.put(True)
            print(client_socket)
            client_socket.send('### Client out.'.encode())
            break
        else:
            ended.put(False)
        client_socket.send(f"{_in}".encode())
    print('send end')

def gett(ended, client_socket:socket.socket):
    print('gett')
    while True:
        if ended.get():
            break
        # time.sleep(1)
        msg = client_socket.recv(SIZE)
        if not msg:
            print(msg.decode(), end='')
            print(f"\t\t\t({time.strftime('%X')})")
    print('gett end')



# 클라이언트 소켓 설정
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect(SERVER_ADDR)  # 서버에 접속\
    
    queue = Queue()
    ended = Queue()

    myin_trd = threading.Thread(target=myin, args=(queue, ))
    send_trd = threading.Thread(target=send, args=(queue, ended, client_socket))
    gett_trd = threading.Thread(target=gett, args=(ended, client_socket))
    
    myin_trd.start()
    send_trd.start()
    gett_trd.start()

    myin_trd.join()

    queue.put(None)

    send_trd.join()

    ended.put(True)

    gett_trd.join()

    print("ended")