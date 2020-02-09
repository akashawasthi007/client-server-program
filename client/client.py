import socket

server_ip="192.168.43.37"
server_port=8080

if __name__ == '__main__':

    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    address=(server_ip,server_port)
    sock.connect(address)

    msg_received=sock.recv(1024)
    print(msg_received.decode())

    sock.close()
