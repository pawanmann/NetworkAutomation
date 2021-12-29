from netmiko import ConnectHandler

User_input1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.101',
    'username': 'dhiraj',
    'password': 'cisco'
}

User_input2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.102',
    'username': 'dhiraj',
    'password': 'cisco'
}

User_input3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.103',
    'username': 'dhiraj',
    'password': 'cisco'
}

User_List = [User_input1, User_input2] #User_input3]

for devices in User_List:
    net_connect = ConnectHandler(**devices)
    for n in range (2,21):
       print ("Creating VLAN " + str(n))
       Vlan_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
       output = net_connect.send_config_set(Vlan_commands)
       print (output)

