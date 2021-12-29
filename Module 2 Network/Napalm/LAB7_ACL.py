import json
from napalm import get_network_driver
driver = get_network_driver('ios')
ios = driver(hostname='192.168.1.226',username='dhiraj', password='cisco')
ios.open()

print ('Accessing 192.168.1.226')
ios.load_merge_candidate(filename='BGP.txt')
ios.commit_config()
ios.close()