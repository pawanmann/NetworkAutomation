from napalm import get_network_driver

driver=get_network_driver('ios')
optional_args={'secret':'cisco'}
ios=driver(hostname='192.168.122.203',username='dhiraj',password='cisco',optional_args=optional_args)
ios.open()
print(dir(ios))
ios.close()
