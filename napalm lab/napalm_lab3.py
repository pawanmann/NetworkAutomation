

from napalm import get_network_driver
from pprint import pprint

driver=get_network_driver('ios')
optional={'secret':'cisco','port':22}
with open ('devices.txt') as file:
    for ip in file:
        ip=ip.strip()
        cisco_device={
            'hostname':ip,
            'username':'pawan',
            'password':'cisco',
            'optional_args':optional
        }

        ios=driver(**cisco_device)
        ios.open()
        output=ios.ping('192.168.75.11')
        # for i in output:
        #     for j in output.values():
        #         print(i)

        pprint(output)



        ios.close()