import getpass
import telnetlib,os

user=input("Enter the username: ")
password=getpass.getpass()

HOST="192.168.122.101"

tn=telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii')+b"\n")

if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii')+b"\n")

print("*"*30+"\nWelcome to Automation world\n"+"*"*30)

print(f"I am inside {HOST}")
tn.write(b"enable\n")
tn.write(b"cisco\n")
tn.write(b"config t\n")
for i in range(2,10):
    tn.write(b"vlan %s\n"%str(i).encode())
    tn.write(b"name python_%s\n"%str(i).encode())

tn.write(b"end\n")
tn.write(b"exit\n")
print(tn.read_all().decode('ascii'))















