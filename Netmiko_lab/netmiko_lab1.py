import os

from netmiko import ConnectHandler

connection=ConnectHandler(ip='192.168.75.10',port =22, username='pawan',password='cisco',device_type='cisco_ios')

output=connection.send_command('sh run')
print(output)
connection.disconnect()

