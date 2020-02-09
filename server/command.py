

def run_command(mysocket):
    print("[+] running commands")

    while True:
        command=input(">> ")
        mysocket.send_data(command)
        if command=="stop":
            break
        result=mysocket.receive_comnd_result()
        print(result)
