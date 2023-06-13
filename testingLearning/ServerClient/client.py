import socket

# 접속 정보 설정
SERVER_IP = '110.76.69.91'
SERVER_PORT = 5050
SIZE = 1024
SERVER_ADDR = (SERVER_IP, SERVER_PORT)

# 클라이언트 소켓 설정
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect(SERVER_ADDR)  # 서버에 접속\
    send_msg = input('your messege: ')
    client_socket.send(send_msg.encode())  # 서버에 메시지 전송
    msg = client_socket.recv(SIZE)  # 서버로부터 응답받은 메시지 반환
    print("resp from server : {}".format(msg.decode()))  # 서버로부터 응답받은 메시지 출력