import sys,getpass,os
import telnetlib,time


HOST="192.168.1.201"
user =os.environ.get('DB_USER')

password=os.environ.get('DB_PWD')

path=os.mkdir("Config")

print("\nThis code will save the configuration of the device\n")

print(f"\nI am working on {HOST} device now")
tn = telnetlib.Telnet(HOST)
tn.read_until(b"Username: ")
tn.write(user.encode('ascii') +b"\n")

if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"terminal length 0\n")
tn.write(b"sh run\n")

tn.write(b"exit\n")
read=tn.read_all().decode('ascii')

with open("Config\Switch %s.txt"%HOST,'w' ) as W:
    W.write(read)

print(" I have done your task\n")

