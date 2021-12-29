import json
from napalm import get_network_driver

driver = get_network_driver('ios')
optional_args={'secret':'cisco'}
Device_list=['192.168.1.226','192.168.1.92']
for ip in Device_list:
    print(f"Connection to: {ip}")
    ios = driver(hostname=ip , username='dhiraj', password='cisco',optional_args=optional_args)
    ios.open()
    print("Rolling Back")
    ios.rollback()
    ios.close()