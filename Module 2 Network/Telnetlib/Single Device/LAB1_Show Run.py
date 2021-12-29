import sys,getpass
import telnetlib

user = "dhiraj"
password= "cisco"

HOST="192.168.122.101"
tn=telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode() +b"\n")

if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode() + b"\n")

print(b"Working........")
tn.write(b"terminal length 0\n")
tn.write(b"sh ip int br\n")
tn.write(b"exit\n")
print(tn.read_all().decode())
