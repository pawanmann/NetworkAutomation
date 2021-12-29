from netmiko import ConnectHandler
iosv_l2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.230',  #enable password has set
    'username': 'dhiraj',
    'password': 'cisco',
    'secret': 'cisco'
}

net_connect = ConnectHandler(**iosv_l2)
print('Entering the enable mode...')
net_connect.enable()

print(net_connect.find_prompt())
output = net_connect.send_command('show ip int brief')
print (output)

# this method receives a list of commands to send to the device

#config_commands='ip ssh version 2;access-list 1 permit any;ip domain-name network-automation.io'
# in enters automatically into global config mode and exists automatically at the end
# config_commands='''int loop 0
# ip address 1.1.1.1 255.255.255.0
# no shut'''
#config_commands = ['int loop 0', 'ip address 1.1.1.1 255.255.255.0']
#O= config_commands.split('\n')
output = net_connect.send_config_set(O)

print (output)

'''
## VARIATIONS
## 1.
cmd = 'ip ssh version 2;access-list 1 permit any;ip domain-name network-automation.io'
net_connect.send_config_set(cmd.split(';')) 
# in enters automatically into global config mode and exists automatically at the end
print(net_connect.find_prompt())

net_connect.send_command('write memory')
'''

print('Closing connection')
net_connect.disconnect()




