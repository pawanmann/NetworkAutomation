from netmiko import ConnectHandler
import time
import threading

start=time.time()

with open('../Netmiko/devices.txt') as f:
    devices = f.read().splitlines()

for ip in devices:
    User_input = {
            'device_type': 'cisco_ios',
            'ip': ip,
            'username': 'dhiraj',
            'password': 'cisco'
        }
    connection = ConnectHandler(**User_input)
    print('Entering the enable mode...')
    connection.enable()

    output = connection.send_command('show run')
    # print(output)
    # creating the backup filename (hostname_date_backup.txt)
    prompt = connection.find_prompt()
    hostname = prompt[0:-1]
    # print(hostname)

    # getting the current date (year-month-day)
    from datetime import datetime
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day

    # creating the backup filename (hostname_date_backup.txt)
    filename = f'{hostname}_{year}-{month}-{day}_backup.txt'

    # writing the backup to the file
    with open(filename, 'w') as backup:
        backup.write(output)
        print(f'Backup of {hostname} completed successfully')
        print('#' * 30)

    print('Closing connection')
    connection.disconnect()

end=time.time()
print(end-start)