import os

from netmiko import ConnectHandler

#connection=ConnectHandler(ip='192.168.75.10',port =22, username='pawan',password='cisco',device_type='cisco_ios')
cisco_device={
    'device_type':'cisco_ios',
    'host':'192.168.75.11',
    'port':22,
    'username':os.environ.get('DB_USER'),
    'password':os.environ.get('DB_PWD'),
    'secret':'cisco'
}
connection=ConnectHandler(**cisco_device)
print(connection.find_prompt())
prompt=connection.find_prompt()
# prompt=list(prompt)
# if prompt[-1]=='>' :
if '>' in prompt:
    print('Entering enable mode')
    connection.enable()  #if enable mode on on device
# output=connection.send_command('sh ver | i up')
# print(connection.check_config_mode())
# connection.config_mode()
# print(connection.check_config_mode())
# output=connection.send_config_set('int lo 50')
# output=connection.send_config_set('ip address 50.50.50.50 255.255.255.0')
# output=connection.send_command('sh ip int brief')

config_commands=['int lo 50','ip add 50.50.50.50 255.255.255.0']
output=connection.send_config_set(config_commands)
output1=connection.send_command(' sh ip int brief')
print(output)
print(output1)
connection.disconnect()

