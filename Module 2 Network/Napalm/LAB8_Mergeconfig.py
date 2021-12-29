import json
from napalm import get_network_driver

driver = get_network_driver('ios')
optional_args={'secret':'cisco'}
ios = driver(hostname='192.168.1.226', username='dhiraj', password='cisco',optional_args=optional_args)
ios.open()

print('Accessing 192.168.1.226')

ios.load_merge_candidate(filename='../Live/Napalm/ACL1.txt')

diffs = ios.compare_config()

if len(diffs) > 0:
    ###Run later on
    print(diffs)
    ios.commit_config()
else:
    print('No changes required.')
    ios.discard_config()

ios.close()