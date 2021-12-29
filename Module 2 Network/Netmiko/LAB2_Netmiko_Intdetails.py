from netmiko import Netmiko

connection = Netmiko(host='192.168.1.230',port=22,username="dhiraj",password='cisco',secret='cisco',device_type='cisco_ios')

#output=connection.send_command("sh ip int br") #Inside the user exec mode
output=connection.send_command("sh run") #Inside the Priv. Exce mode command
#output=connection.send_command("sh version | i uptime") #Inside the Priv. Exce mode command
print(output)

print("Closing Connection")
connection.disconnect()


