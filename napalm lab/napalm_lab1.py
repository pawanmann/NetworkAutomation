import json

from napalm import get_network_driver
from pprint import pprint
driver=get_network_driver('ios')
optional={'secret':'cisco','port':22}
ios=driver(hostname='192.168.75.10',username='pawan',password='cisco',optional_args=optional)
ios.open()
# output=ios.get_arp_table()
# output=ios.get_mac_address_table()
output=ios.get_facts()
output=ios.get_vlans()
# for i in output:
#     print(f"MAC: {i['mac']} \nInterface: {i['interface']} \nIP :{i['ip']}\n\n")
print(output)
# for i in output:
#     print(i)

# dump=json.dumps(output,indent=4,sort_keys=True)
# print(dump)


ios.close()