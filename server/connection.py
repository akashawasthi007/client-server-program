import socket
DELIMETER="<END_OF_RESULT>"

CHUNK=4*1024

class serverconnection:
    def __init__(self):
        # creates a tcp client_socket
        self.socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    def create_connection(self,ip="",port=8080):
        self.server_ip=ip
        self.server_port=port
        self.address=(self.server_ip,self.server_port)
        self.socket.bind(self.address)

    def listen_connection(self,backlog=1):
        self.socket.listen(backlog)

    def accept_connection(self):
        self.client_conn,self.client_add=self.socket.accept()
        print("connection established with "+self.client_add[0] +"on port "+str(self.client_add[1]))
        return (self.client_conn,self.client_add)

    def send_data(self,user_input):
        user_input_inbytes=bytes(user_input,"utf-8")
        self.client_conn.send(user_input_inbytes)

    def receive_data(self):
        received_user_data  =  self.client_conn.recv(CHUNK)
        self.data=received_user_data.decode('utf-8')
        return self.data

    def receive_comnd_result(self):
        print("[+] getting command result")
        resul=b''
        while True:
            chunkn=self.client_conn.recv(CHUNK)
            if chunkn.endswith(DELIMETERE.encode()):
                chunkn+=chunkn[:-len(DELIMETER)]
                resul+=chunkn
            resul+=chunkn
        print(resul.decode())

    def close(self):
        self.socket.close()
