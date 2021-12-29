import paramiko, time

ssh_client=paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

O=open('WTD.txt','r')

for line in O:
    IP=line.strip()
    print(f"Working on {IP} ")
    Switch={'hostname':IP,'username':"dhiraj",'port':22,'password':"cisco"}
    ssh_client.connect(**Switch,look_for_keys=False,allow_agent=False)
    shell=ssh_client.invoke_shell()
    shell.send("conf t\n")
    shell.send('int loopback 1\n')
    shell.send('ip address 1.1.1.1 255.255.255.0\n')
    shell.send('router ospf 1\n')
    shell.send('net 0.0.0.0 0.0.0.0 area 0\n')
    shell.send('end\n')
    shell.send('terminal length 0\n')
    shell.send('sh ip protocols\n')
    time.sleep(2)

    output=shell.recv(65535).decode()
    print(output)

if ssh_client.get_transport().is_active():
    print("Closing connections")
    ssh_client.close()


