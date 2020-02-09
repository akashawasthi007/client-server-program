from connection import clientconnection
from handle import handleconn

if __name__ == '__main__':
    mysocket=clientconnection()

    mysocket.Connect("192.168.43.28",123)
#    print(mysocket.received_data())
#    mysocket.send_data("this is the client")
#S    mysocket.close()
    handleconn(mysocket)

    mysocket.close()
