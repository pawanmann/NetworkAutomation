from netmiko import ConnectHandler

# reading the devices ip address from a file into a list (each ip on its own line)
with open("devices.txt") as file:
    devices = file.read().splitlines()

device_list=[] #or list()

for IP in devices:
    User_input = {
        'device_type': 'cisco_ios',
        'ip': IP,
        'username': 'dhiraj',
        'password': 'cisco'
    }
    device_list.append(User_input)

file=input(f"Enter the file name of config file name:  ")

for Login in device_list:
    net_connect=ConnectHandler(**Login)
    print("Entering into the enable mode")
    net_connect.enable()
    print(f"Running commands from file: {file} on device: {Login['ip']}")
    output=net_connect.send_config_from_file(file)
    print(output)
    print("Closing Connections")
    net_connect.disconnect()
    print("#"*30)

print(f"{'#'*30}\n\tAutomation Completed\n{'#'*30} ")

'''
#Show ip ospf negibour
'''
