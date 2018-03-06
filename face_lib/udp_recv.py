from socket import *
import numpy as np


class UdpGetVideo:
    def __init__(self):
        self.HOST = ''
        self.PORT = 21567
        self.BUF = 1024 * 100
        self.ADDR = (self.HOST, self.PORT)

        # socket对象实例化
        self.udpSerSock = socket(AF_INET, SOCK_DGRAM)
        # 与客户端绑定
        self.udpSerSock.bind(self.ADDR)

    def receive(self):
        data, addr = self.udpSerSock.recvfrom(self.BUF)
        data = np.fromstring(data, dtype=np.uint8)
        return data

    def close(self):
        self.udpSerSock.close()

