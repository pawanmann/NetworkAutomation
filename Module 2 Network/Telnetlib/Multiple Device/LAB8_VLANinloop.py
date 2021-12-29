import sys, getpass
import telnetlib, time, os

user = os.environ.get('DB_USER')
password = os.environ.get('DB_PWD')

print("\n This will create the VLAN on switch")

for j in range(201,203):
    HOST = "192.168.1." + str(j)

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