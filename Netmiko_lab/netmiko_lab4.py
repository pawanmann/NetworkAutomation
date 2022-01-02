import os
from netmiko import ConnectHandler

cisco_device={
    'device_type':'cisco_ios',
    'host':'192.168.75.11',
    'port':22,
    'username':os.environ.get('DB_USER'),
    'password':os.environ.get('DB_PWD'),
    'secret':'cisco'
}
connection=ConnectHandler(**cisco_device)
print('starting the session')
prompt=connection.find_prompt()
if '>' in prompt:
    print('Entering enable mode')
    connection.enable()  # if enable mode on on device
print('sending command to switch')
output=connection.send_config_from_file('config.txt')
print(output)
connection.disconnect()