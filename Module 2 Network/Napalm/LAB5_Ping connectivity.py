import json

from napalm import get_network_driver

driver=get_network_driver('ios')
optional_args={'secret':'cisco'}
ios=driver('192.168.122.204','dhiraj','cisco',optional_args=optional_args)
ios.open()
#output=ios.ping("192.168.122.205")

##Extended ping ############
output=ios.ping(destination="192.168.122.203",count=2,source="2.2.2.2")

ping=json.dumps(output,indent=4)
print(ping)

ios.close()
