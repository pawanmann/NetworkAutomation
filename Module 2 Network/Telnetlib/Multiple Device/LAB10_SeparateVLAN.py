import sys, getpass
import telnetlib, time, os

user = input("Enter the username: ")
password = getpass.getpass()
f=open("WTD.txt",'r')
for line in f:
    HOST=line.strip()
    print("\n This will create the VLAN on switch")

    print("\nI am working on switch#%s device now" % HOST)

    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode() + b"\n")

    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode() + b"\n")

    tn.write(b"config t\n")
    for i in range(2, 5):
        tn.write(b"vlan %s\n" % (str(i).encode()))
        tn.write(b"name python_%s\n" %(str(i).encode()))

    tn.write(b"end\n")
    tn.write(b"write\n")
    tn.write(b"exit\n")

    print(tn.read_all().decode())

print(" I have done your task\n")