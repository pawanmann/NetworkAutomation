import os

import paramiko,time,getpass

ssh_client=paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# username=input("enter username: ")
# password = getpass.getpass("enter Password: ")  # need to debug in getpass case instead of run

username=os.environ.get("DB_USER")
password=os.environ.get("DB_PWD")
open=open('WTD.txt')

for Device in open:
    Device=Device.strip()

    print(f"Connecting to {Device}")
    Node={'hostname':Device, 'username':username, 'password':password, 'port':22}
    ssh_client.connect(**Node)

    shell= ssh_client.invoke_shell()
    shell.send("terminal len 0\n")
    shell.send("sh ip int brief\n")
    time.sleep(2)

    output=shell.recv(65535)
    output=output.decode('ascii')


    if ssh_client.get_transport().is_active()==True:
        print("close connection")
        print(output)