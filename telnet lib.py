
import telnetlib

HOST="192.168.75.100"
user = "pawan"
password = "cisco"
# user = str(input("Enter the telnet username: "))
# password = str(input("Enter the telnet password: "))

tn=telnetlib.Telnet(HOST)
tn.read_until(b"Username: ")
tn.write(user.encode('ascii') +b"\n")


if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') +b"\n")
print("*"*30 + " Welcome to Automation "+ "*"*30)
print(f"i am inside {HOST}")
# print(tn.write(b" terminal len 0\n"))
# print(tn.write(b" sh run\n"))
# print(tn.write(b"exit\n"))



tn.write(b"conf t\n")
tn.write(b"int lo 0\n")
tn.write(b"ip add 10.10.10.10 255.255.255.0\n")
tn.write(b"int lo 1\n")
tn.write(b"ip add 20.20.20.20 255.255.255.0\n")
tn.write(b"int lo 3\n")
tn.write(b"ip add 30.30.30.30 255.255.255.0\n")
tn.write(b"end\n")
tn.write(b"wr me\n")
tn.write(b"sh ip int brief\n")
tn.write(b"exit\n")

print(tn.read_all().decode())