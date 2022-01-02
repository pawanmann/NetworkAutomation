import os
from netmiko import ConnectHandler

Config_file=input("Enter the filename: ")

with open('devices.txt') as file:
    for ip in file:
        ip=ip.strip()
        Cisco_device={
            'device_type':'cisco_ios',
            'ip':ip,
            'username':'pawan',
            'password':'cisco',
            'port':22,
            'secret':'cisco'
        }
        Connection=ConnectHandler(**Cisco_device)
        print('staring the Session')
        if '>' in Connection.find_prompt():
            print("Entering in to enable mode")
            Connection.enable()
        print(f"Running command from file: {Config_file} on device{Cisco_device['ip']} ")
        output=Connection.send_config_from_file(Config_file)
        print(output)
        print('closing connection')
        Connection.disconnect()

    print(f"{'*'*30}\n\t Automation Completed \n{'*'*30}")
