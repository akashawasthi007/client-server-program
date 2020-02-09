import socket

server_ip=""  # your private ip address
server_port=8080   # any port less than 1024

if __name__ == '__main__':
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM) # for connecting two nodes in a server
    # socket.Af_INET for ip address v4
    # socket.SOCK_STREAM is for tcp packets

    address=(server_ip,server_port)

    sock.bind(address)  # bind our ip with cocket
    sock.listen(1) #allow numbet of connections in a queue

    print("+ waiting for incoming connection on port :",server_port)#waiting for incoming conections on our server port
    client_socket,client_add=sock.accept()# accept the client's socket and client's address
    print("connection established :",client_add)
    msg="this the server speaking"

    client_socket.send(msg.encode())#send msg to client predecting to be a server
    client_socket.close()# for closing the connections
    sock.close()
