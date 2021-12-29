import paramiko

# creating an ssh client object
ssh_client = paramiko.SSHClient()
#print(type(ssh_client))

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print('Connecting to 192.168.122.101')
ssh_client.connect(hostname='192.168.122.101', port=22, username='dhiraj', password='cisco')

# checking if the connection is active
print(ssh_client.get_transport().is_active())

# sending commands
print('Closing connection')
ssh_client.close()