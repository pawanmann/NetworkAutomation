from netmiko import ConnectHandler

connection=ConnectHandler(ip='192.168.75.50',port =22, username='pawan',password='cisco',device_type='cisco_asa',secret='cisco')

output=connection.send_command('sh ver | i up')
print(output)
connection.disconnect()