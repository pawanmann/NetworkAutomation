import json

from napalm import get_network_driver
IP='192.168.1.221'
cisco_device = {
       'hostname': IP,
       'username': 'dhiraj',
       'password': 'cisco',
        'optional_args': {'secret':'cisco'}
}

driver=get_network_driver('ios')
ios=driver(**cisco_device)
ios.open()

#output=ios.get_facts() ##It will return the output of methods of the device
output=ios.get_arp_table()
#output=ios.get_interfaces()
#output=ios.get_interfaces_ip()
#output=ios.get_interfaces_counters()
#output=ios.get_users()
#output= ios.ping('192.168.1.200')

for i in output:
    print(i)
# dump=json.dumps(output,indent=4)
# print(dump)

ios.close()
