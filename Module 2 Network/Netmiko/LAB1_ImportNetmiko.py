from netmiko import Netmiko

connection = Netmiko(ip='192.168.1.221',port=22,username='dhiraj',password='cisco',device_type='cisco_ios')

output=connection.send_command("sh int ip br") #Inside the user exec mode

print(output)

print("Closing Connection")
connection.disconnect()