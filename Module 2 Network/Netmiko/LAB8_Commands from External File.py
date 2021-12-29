'''
terminal monitor
debug ip ospf events
'''

from netmiko import ConnectHandler

User_input={
    'device_type': 'cisco_ios',
    'ip': '192.168.1.221',
    'username': 'dhiraj',
    'password': 'cisco'

}

net_connect=ConnectHandler(**User_input)
print("Starting Connections")
net_connect.enable()

print("Sending Commands.....")
Output= net_connect.send_config_from_file('ospf.txt')
print(Output)
print("Closing Connections")
net_connect.disconnect()