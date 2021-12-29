import paramiko,time

def connect(IP,Port,User,Passwd):
    global ssh_client
    ssh_client=paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(f"Working on {IP}")
    ssh_client.connect(hostname=IP,port=Port,username=User,password=Passwd,look_for_keys=False, allow_agent=False)
    return ssh_client

def get_ssh(ssh_client):
    shell= ssh_client.invoke_shell()
    return shell

def send_command(shell,command,timeout=1):
    print(f"Sending command: {command} ")
    shell.send(command+"\n")
    time.sleep(timeout)

def output(shell,n=65535):
    return shell.recv(n).decode('ascii')

def close():
    if ssh_client.get_transport().is_active():
        print("Closing connections")
        ssh_client.close()

with open("WTD.txt", 'r') as R:
    for line in R:
        Strip=line.strip()
        SW1 = {'IP':Strip,'Port':22 ,'User':'dhiraj','Passwd':'cisco'}
        conn=connect(**SW1)
        shell= get_ssh(conn)
        with open("Command.txt", 'r') as R1:
            for line1 in R1:
                Strip1=line1.strip()
                send_command(shell, Strip1)
            Catch=output(shell)
            with open(f'Output of switch{Strip}.txt','w') as C:
                C.write(Catch)
        close()
