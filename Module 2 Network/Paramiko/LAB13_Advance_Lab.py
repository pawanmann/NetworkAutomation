import paramiko,time

def connect(hostname,Port,User,Passwd):
    global ssh_client
    ssh_client=paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(f"Working on {hostname}")
    ssh_client.connect(hostname=hostname,port=Port,username=User,password=Passwd,look_for_keys=False, allow_agent=False)
    return ssh_client

def get_ssh(ssh_client):
    shell= ssh_client.invoke_shell()
    return shell

def send_command(shell,command,timeout=10):
    print(f"Sending command: {command} ")
    shell.send(command+"\n")
    time.sleep(timeout)

def output(shell,n=65535):
    return shell.recv(n).decode('ascii')

def close():
    if ssh_client.get_transport().is_active():
        print("Closing connections")
        ssh_client.close()

if __name__=='__main__':
    SW1 = {'hostname':'192.168.1.221','Port':22 ,'User':'dhiraj','Passwd':'cisco'}
    conn=connect(**SW1)
    shell= get_ssh(conn)
    send_command(shell,'terminal length 0')
    send_command(shell,'show run')
    send_command(shell,'exit')
    Output=output(shell)
    with open(f'Output of switch{SW1["IP"]}.txt', 'w') as C:
        C.write(Output)
    close()
