import sys,getpass,os
import telnetlib,time

Directory=r'F:\Python\Classes\Skilled inspiration Acedemy\Python Auto\Labs\Telnetlib'

HOST="192.168.122.102"
user =input("Enter your username: ")
password=getpass.getpass()
L1=os.listdir(Directory)

if "Config" in L1:
    os.rmdir(Directory +"\Config")

path=os.mkdir(Directory +"\Config")

print("\nThis code will save the configuration of the device\n")

print("\nI am working on %s device now" %HOST)
tn = telnetlib.Telnet(HOST)
tn.read_until(b"Username: ")
tn.write(user.encode('ascii') +b"\n")

if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write(b"cisco\n")
tn.write(b"terminal length 0\n")
tn.write(b"sh run\n")

tn.write(b"exit\n")
read=tn.read_all().decode('ascii')

with open(Directory + "\Config\Switch %s.txt"%HOST,'w' ) as W:
    W.write(read)

print(" I have done your task\n")

