from connection import serverconnection
from handle import handleconn
#from command import run_command1


if __name__ == '__main__':

    mysocket=serverconnection()
    mysocket.create_connection("",123)
    mysocket.listen_connection()
    mycon,_=mysocket.accept_connection()
#    mysocket.send_data("this is the server speaking")
#    print(mysocket.receive_data())
    handleconn(mysocket)
    mycon.close()
