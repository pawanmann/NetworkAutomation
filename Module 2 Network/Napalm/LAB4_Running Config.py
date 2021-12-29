import json

from napalm import get_network_driver

driver=get_network_driver('ios')
optional_args={'secret':'cisco'}
ios=driver('192.168.1.221','dhiraj','cisco',optional_args=optional_args)
ios.open()

output=ios.get_config()
#print(output.keys())
#print(output.values())
for item in output.values():
    print(item)
    # read=open("args.txt",'w')
    # read.write(item)

ios.close()
