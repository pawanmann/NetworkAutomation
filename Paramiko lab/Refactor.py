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

SW1={'IP':'192.168.75.10','Port':22,'User':os.environ.get('DB_USER'),'Password':os.environ.get('DB_PWD')}
Conn=connect(**SW1)
shell=get_ssh(Conn)
send_command(shell,'config t')
send_command(shell,'vlan 100')
send_command(shell,'name Accounts')
send_command(shell,'vlan 200')
send_command(shell,'name Sales')
send_command(shell,'end')
send_command(shell,'terminal len 0')
send_command(shell,'sh vlan brief')

Catch=output(shell)

with open("Vlan %s.txt"%SW1['IP'],'w') as W:
    W.write(Catch)

# print(Catch)

close()

