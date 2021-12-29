import sys,getpass,os
import telnetlib,time

try:
    user =input("Enter your username: ")
    password=getpass.getpass()
    f=open("WTD.txt",'r')
    path=os.mkdir("Config")
    print("\nThis code will save the configuration of the device\n")

    for line in f:
        HOST = line.strip()
        print("\nI am working on %s device now" %HOST)
        tn = telnetlib.Telnet(HOST)
        tn.read_until(b"Username: ")
        tn.write(user.encode() +b"\n")

        if password:
            tn.read_until(b"Password: ")
            tn.write(password.encode() + b"\n")

        tn.write(b"terminal length 0\n")
        tn.write(b"sh run\n")

        tn.write(b"exit\n")
        read=tn.read_all().decode()

        with open("Config\Switch %s.txt"%HOST,'w' ) as W:
            W.write(read)

    print(" I have done your task\n")

except FileExistsError:
    print("Config folder is already exist")