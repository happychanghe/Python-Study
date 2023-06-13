import socket
import asyncio

# TODO: server와 클라이언트 분리

# 통신 정보 설정
IP = '192.168.0.12'
PORT = 5050
SIZE = 1024
ADDR = (IP, PORT)

async def mymessege():
    mmsg = input('> ')
    return mmsg
    pass

async def hermessege(client_socket):
    hmsg = client_socket.recv(SIZE)
    return hmsg
    pass

async def lloopp(client_socket, client_addr):
    while True:
        mmsg = await mymessege()
        hmsg = await hermessege()
        print("[{}] message : {}".format(client_addr,hmsg.decode()))
        client_socket.sendall(mmsg.encode())
        if "ONO" in mmsg:
            client_socket.sendall('### Server closed.'.encode())
            client_socket.close()
            break 
    pass

# 서버 소켓 설정
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind(ADDR)  # 주소 바인딩
    server_socket.listen()  # 클라이언트의 요청을 받을 준비

    client_socket, client_addr = server_socket.accept()

    # 무한루프 진입
    loop = asyncio.get_event_loop()             # 이벤트 루프를 얻음
    loop.run_until_complete(lloopp)    # print_add가 끝날 때까지 이벤트 루프를 실행
    loop.close()

    client_socket.close()  # 클라이언트 소켓 종료