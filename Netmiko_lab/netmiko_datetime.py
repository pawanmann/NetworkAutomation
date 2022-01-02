import os,time

from netmiko import ConnectHandler
from datetime import datetime

Now=datetime.now()
start= time.time()

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
        filename=f"{hostname}_{Now.day}_{Now.month}_{Now.year}_{Now.hour}_{Now.minute}_{Now.second}"+'backup.txt'
        with open(filename,'w') as backup:
            backup.write(output)
            print(f"Backup of {hostname} has been completed")
        # print(output)
        print('closing connection')
        os.startfile(filename)
        Connection.disconnect()
end=time.time()
time_take=end-start
print(time_take)
print(f"{'*'*30}\n\t Automation Completed \n{'*'*30}")
