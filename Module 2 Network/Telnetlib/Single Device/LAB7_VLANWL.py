import sys, getpass
import telnetlib, time,os

# user = input("Enter your username: ")
# password = getpass.getpass()
user = os.environ.get('DB_USER')
password = os.environ.get('DB_PWD')

print("*"*30+"\n"+"Welcome to automation world"+"\n"+"*"*30)

for j in range(101,102):
    HOST = "192.168.122." + str(j)

    print("\nI am working on switch#%s device now" % HOST)

    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode() + b"\n")

    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode() + b"\n")

    tn.write(b"config t\n")
    for i in range(2, 30):
        tn.write(b"vlan %s\n" % (str(i).encode()))
        tn.write(b"name python_%s\n" % (str(i).encode()))

    tn.write(b"end\n")
    tn.write(b"exit\n")

    print(tn.read_all().decode())

print(" I have done your task\n")