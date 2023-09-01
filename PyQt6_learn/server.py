import json
import socket
import threading
import time
from data import DataSource


class ClientThread(threading.Thread):
    def __init__(self, client, addr):
        super(ClientThread, self).__init__()
        self.client = client
        self.addr = addr

        self.login_user = None

        print('{} 连接成功！'.format(addr))
        self.client.send(b'OK 200')

    def run(self) -> None:
        while True:
            b_msg = self.client.recv(1024*8) # 等待接收客户端信息
            if b_msg == b'exit':
                break

            # 解析命令
            try:
                self.parse_cmd(b_msg.decode('utf-8'))
            except:
                self.client.send(b'Error')

        self.client.send(b'closing')
        print('{} 断开连接'.format(self.addr))

    def parse_cmd(self, cmd):
        print('接收命令-----', cmd)
        if cmd.startswith('login'):
            # login username pwd
            _, name, pwd = cmd.split()
            for item in datas:
                if item['name'] == name and item['pwd'] == pwd:
                    self.login_user = item

            if self.login_user is not None:
                self.client.send(b'OK 200')
            else:
                self.client.send(b'not exist user')
        else:
            if self.login_user is None:
                self.client.send(b'no login session')

            elif cmd.startswith('add'):
                # add 100
                blance = float(cmd.split()[-1])
                self.login_user['blance'] += blance
                self.client.send(b'OK 200')
            elif cmd.startswith('sub'):
                # sub 100
                blance = float(cmd.split()[-1])
                self.login_user['blance'] -= blance
                self.client.send(b'OK 200')
            elif cmd.startswith('get'):
                self.client.send(json.dumps(self.login_user, ensure_ascii=False).encode('utf-8'))


if __name__ == '__main__':

    datas = DataSource().load()

    # 创建socket应用服务
    server = socket.socket()
    server.bind(('localhost', 18900))  # 绑定主机IP和Host
    server.listen()

    print('中心服务已启动\n等待客户端连接...')
    while True:
        client, addr = server.accept()
        ClientThread(client, addr).start()

        time.sleep(0.5)