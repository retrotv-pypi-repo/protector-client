import socket

"""
AF_INET: IP v4 사용
AF_INET6: IP v6 사용

SOCK_STREAM: 연결 지향형 소켓
SOCK_DGRAM: 비연결 지향형 소켓 (데이터 손실 가능성 있음)
"""
from socket import AF_INET, SOCK_STREAM


class Socket:
    def __init__(self, addr: str, port: int):
        self.addr = addr
        self.port = port
        self.client = socket.socket(AF_INET, SOCK_STREAM)

    def run(self):
        self.client.connect((self.addr, self.port))

    def send_message(self, msg: str):
        self.client.send(msg.encode())
        return self.client.recvmsg(1024)
