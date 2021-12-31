import os

import paramiko,time

def connect(IP,Port,User,Password):
    global ssh_client
    ssh_client=paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(f"Working for {IP}")
    ssh_client.connect(hostname=IP,port=Port,username=User,password=Password)
    return ssh_client

def get_ssh(ssh_client):
    shell=ssh_client.invoke_shell()
    return shell

def send_command(shell,command,timeout=5):
    print(f"Sending command: {command}")
    shell.send(command+"\n")
    time.sleep(timeout)

def output(shell,n=65535):
    return shell.recv(n).decode('ascii')

def close():
    if ssh_client.get_trasport().is_active():
        print('Close connection')
        ssh_client.close()



