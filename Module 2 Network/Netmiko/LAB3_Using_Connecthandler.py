from netmiko import ConnectHandler
# creating a dictionary for the device to connect to
cisco_device = {
       'device_type': ' cisco_ios',     #device type from https://github.com/ktbyers/netmiko/blob/master/netmiko/ssh_dispatcher.py
       'ip': '192.168.1.221',
       'username': 'dhiraj',
       'password': 'cisco',
       'port': 22,         # optional, default 22
       'secret':'cisco'   # this is the enable password
       }

# connecting to the device and returning an ssh connection object
connection = ConnectHandler(**cisco_device)

# # sending a command and getting the output
output = connection.send_command('sh run')
print(output)

# closing the connection
print('Closing connection')
connection.disconnect()