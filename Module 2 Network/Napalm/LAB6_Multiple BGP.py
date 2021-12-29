import json
import time

from napalm import get_network_driver
BGPlist=["192.168.1.226","192.168.1.92"]
for IP in BGPlist:
    print(f"Connecting to {IP}")
    driver=get_network_driver('ios')
    optional={'secret':'cisco'}
    ios=driver(IP,username='dhiraj',password='cisco',optional_args=optional)
    ios.open()
    output=ios.get_bgp_neighbors()

    dump=json.dumps(output,indent=4)
    print(dump)

    ios.close()