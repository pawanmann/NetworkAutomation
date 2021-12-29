import paramiko
import time,os
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# creating a dictionary for each device to connect to
router1 = {'hostname': '192.168.1.221', 'port': '22', 'username':os.environ.get('DB_USER'), 'password': os.environ.get('DB_PWD')}
router2 = {'hostname': '192.168.1.222', 'port': '22', 'username':'dhiraj', 'password':'cisco'}
#router3 = {'hostname': '192.168.1.93', 'port': '22', 'username':'dhiraj', 'password':'cisco'}

# creating a list of dictionaries (of devices)
routers = [router1, router2]

# iterating over the list (over the devices) and backup the config
for router in routers:
    print(f'Connecting to {router["hostname"]}')
    ssh_client.connect(**router, look_for_keys=False, allow_agent=False)
    shell = ssh_client.invoke_shell()

    shell.send('conf t\n')
    shell.send('int loopback 1\n')
    shell.send('ip address 1.1.1.1 255.255.255.0\n')
    shell.send('router ospf 1\n')
    shell.send('net 0.0.0.0 0.0.0.0 area 0\n')
    shell.send('end\n')
    shell.send('terminal length 0\n')
    shell.send('sh ip protocols\n')
    time.sleep(2)

    output = shell.recv(10000).decode()
    print(output)

if ssh_client.get_transport().is_active() == True:
    print('Closing connection')
    ssh_client.close()