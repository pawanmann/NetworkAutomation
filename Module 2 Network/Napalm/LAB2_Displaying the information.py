import json

from napalm import get_network_driver

driver=get_network_driver('ios')
optional_args={'secret':'cisco'}
ios=driver('192.168.1.222','dhiraj','cisco',optional_args=optional_args)
ios.open()

output=ios.get_arp_table()
#output=ios.get_mac_address_table()
# print(output)
# for item in output:
#     print(f"MAC: {item['mac']} INTERFACE: {item['interface']} VLAN: {item['vlan']}")
#    print(item)
### convert into readble format ##################

dump=json.dumps(output,sort_keys=True,indent=4)
print(dump)
#
# with open("args.txt",'w') as e:
#     e.write(dump)


ios.close()
