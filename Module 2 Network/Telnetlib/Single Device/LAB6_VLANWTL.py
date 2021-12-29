import sys, getpass,os
import telnetlib, time

user = os.environ.get('DB_USER')
password = os.environ.get('DB_PWD')

print("*"*30+"\n"+"Welcome to automation world"+"\n"+"*"*30)

HOST="192.168.122.101"
print("\n This will create the VLAN on switch")

tn = telnetlib.Telnet(HOST)
tn.read_until(b"Username: ")
tn.write(user.encode() + b"\n")

if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode() + b"\n")

tn.write(b"config t\n")

tn.write(b"vlan 2\n")
tn.write(b"name python_2\n")
tn.write(b"vlan 3\n")
tn.write(b"name python_3\n")
tn.write(b"vlan 4\n")
tn.write(b"name python_4\n")
tn.write(b"end\n")
tn.write(b"write\n")
tn.write(b"exit\n")

print(tn.read_all().decode())

print(" I have done your task\n")