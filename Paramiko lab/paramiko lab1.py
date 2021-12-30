import time

import paramiko
ssh_client=paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  #use for accept authentication of ssh

# ssh_client.connect(hostname='192.168.75.10',username='pawan',password='cisco',port=22)

switch={
    'hostname':'192.168.75.10',
    'port': 22,
    'username':'pawan',
    'password':'cisco'
}

print(f"Connecting to {switch['hostname']}")
a=ssh_client.connect(**switch)

shell=ssh_client.invoke_shell()
shell.send('terminal len 0\n')
shell.send('sh ver | i up \n')
shell.send('sh ip int brief\n')
shell.send('sh run\n')

time.sleep(5)
output=shell.recv(10000)
output=output.decode()
print(output)

if ssh_client.get_transport().is_active() == True:  #True/False
    print("closing connection")



