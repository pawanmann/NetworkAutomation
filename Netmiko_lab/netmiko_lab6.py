import os

from netmiko import ConnectHandler

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
        output=Connection.send_command('sh run')
        prompt=Connection.find_prompt()
        hostname=prompt[0:-1]
        print(hostname)
        filename=hostname+'backup.txt'
        with open(filename,'w') as backup:
            backup.write(output)
            print(f"Backup of {hostname} has been completed")
        # print(output)
        print('closing connection')
        os.startfile(filename)
        Connection.disconnect()

print(f"{'*'*30}\n\t Automation Completed \n{'*'*30}")
