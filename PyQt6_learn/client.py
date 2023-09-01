import socket
import threading


class CenterClient():
    def __init__(self, server, port):
        super().__init__()
        self.server = server
        self.port = port
        self.isConnected = False
        self.client = None

    def connect(self):
        self.client = socket.socket()
        self.client.connect((self.server, self.port))
        msg = self.client.recv(8*1024)
        if msg == b'OK 200':
            print('---连接成功--')
            self.isConnected = True
        else:
            print('---连接失败---')
            self.isConnected = False

    def send_cmd(self, cmd):
        self.client.send(cmd.encode('utf-8'))
        data = self.client.recv(8*1024)
        print('{}命令结果: {}'.format(cmd, data))
        if data == b'Error':
            return '400'
        return data.decode('utf-8')


if __name__ == '__main__':
    client = CenterClient('localhost', 18900)
    client.connect()
    print(client.send_cmd('login disen disen123'))
    # print(client.send_cmd('add 1000'))
    # print(client.send_cmd('sub 50'))
    print(client.send_cmd('get'))