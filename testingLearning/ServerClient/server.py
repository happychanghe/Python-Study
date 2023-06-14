import socket
import time
import threading 
from queue import Queue

# 통신 정보 설정
IP = '192.168.0.12'
PORT = 5050
SIZE = 1024
ADDR = (IP, PORT)

def myin(queue):
    print('myin')
    while True:
        n = input()
        if "OUT" in n: 
            # queue.put(None)
            break
        queue.put(n)
    print('myin end')


def send(queue, ended, client_socket:socket.socket):
    print('send')
    while True:
        _in = queue.get()
        if _in is None:
            # ended.put(True)
            client_socket.sendall('### Server closed.'.encode())
            client_socket.close()
            break
        else:
            ended.put(False)
        client_socket.sendall(f"ych: {_in}".encode())
    print('send end')

def gett(ended, client_socket:socket.socket, client_addr):
    print('gett')
    while True:
        if ended.get():
            break
        # time.sleep(1)
        print(1)
        msg = client_socket.recv(SIZE)
        print(bool(msg), msg, 1)
        if not msg:
            print("[{}] message : {}".format(client_addr,msg.decode()), end='')
            print(f"\t\t\t({time.strftime('%X')})")
    print('gett end')


# 서버 소켓 설정
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind(ADDR)  # 주소 바인딩
    server_socket.listen()  # 클라이언트의 요청을 받을 준비

    # 무한루프 진입
    ''' 
    연결이 끊기면 삭제한다. 
    온 연결이 있으면 받는다. 
    받은 연결은 리스트에 담는다. (나중)

    온 채팅이 있으면 받는다. 
    채팅을 입력하면 보낸다. (채팅이 예약어면 탈출) 

    '''
    print('server started')
    client_socket, client_addr = server_socket.accept()  # 수신대기, 접속한 클라이언트 정보 (소켓, 주소) 반환       ### 기다림
    print(client_addr, 'client connected')

    queue = Queue()
    ended = Queue()


    myin_trd = threading.Thread(target=myin, args=(queue, ))
    send_trd = threading.Thread(target=send, args=(queue, ended, client_socket))
    gett_trd = threading.Thread(target=gett, args=(ended, client_socket, client_addr))

    myin_trd.start()
    send_trd.start()
    gett_trd.start()

    myin_trd.join()

    queue.put(None)

    send_trd.join()

    ended.put(True)

    gett_trd.join()

    print("ended")


