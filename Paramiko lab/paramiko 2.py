import paramiko,time,getpass

ssh_client=paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

username=input("enter username: ")
password = getpass.getpass("enter Password: ")  # need to debug in getpass case instead of run

sw1={'hostname': '192.168.75.10','port':22,'username':username,'password': password,}
sw2={'hostname': '192.168.75.11','port':22,'username':username,'password': password,}

Nodes=[sw1,sw2]

for Device in Nodes:


    print(f"Connecting to {Device['hostname']}")
    ssh_client.connect(**Device)

    shell= ssh_client.invoke_shell()
    shell.send("terminal len 0\n")
    shell.send("sh ip int brief\n")
    time.sleep(2)

    output=shell.recv(65535)
    output=output.decode('ascii')


    if ssh_client.get_transport().is_active()==True:
        print("close connection")
        print(output)