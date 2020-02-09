import socket

CHUNK=4*1024
DELIMETER = "<END_OF_RESULT>"

class clientconnection:
    def __init__(self):
        self.socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    def Connect(self,server_ip,server_port):
        self.socket.connect((server_ip,server_port))
        self.server_ip=server_ip
        self.server_port=server_port

    def received_data(self):
        self.data_in_bytes=self.socket.recv(CHUNK)
        self.data=self.data_in_bytes.decode('utf-8')
        return self.data

    def send_data(self,data):
        self.data_in_bytes=bytes(data,"utf-8")
        self.socket.send(self.data_in_bytes)

    def send_comnd_result(self,command_result):
        data2send=command_result+DELIMETER
        data2send_bytes=data2send.encode()
        self.socket.sendall(data2send_bytes)

    def close(self):
        self.socket.close()
