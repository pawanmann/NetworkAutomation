import json
from napalm import get_network_driver

driver = get_network_driver('ios')


optional_args={'secret':'cisco'}

print(f"Connection to: 192.168.1.226 ")
ios = driver(hostname= '192.168.1.226', username='dhiraj', password='cisco',optional_args=optional_args)
ios.open()

ios.load_merge_candidate(filename='../Live/Napalm/ACL1.txt')
diffs = ios.compare_config()

if len(diffs) > 0:
    print(diffs)
    ios.commit_config()
else:
    print('No ACL changes required.')
    ios.discard_config()

ios.load_merge_candidate(filename='../Live/Napalm/ospf1.txt')
diffs = ios.compare_config()

if len(diffs) > 0:
    print(diffs)
    ios.commit_config()

else:
    print('No OSPF changes required.')
    ios.discard_config()

ios.close()