import telnetlib,os,getpass,sys

L=["192.168.1.101","192.168.1.102"]

user = os.environ.get('DB_USER')
password=os.environ.get('DB_PWD')

for HOST in L:
    tn=telnetlib.Telnet(HOST)
    print(b"Your Automation is working")
    print(b"I am working on ", HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') +b"\n")

    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    tn.write(b"config t\n")
    tn.write(b"int loopback 1\n")
    tn.write(b"ip address 1.1.1.1 255.255.255.255\n")
    tn.write(b"int loopback 2\n")
    tn.write(b"ip address 2.2.2.2 255.255.255.255\n")
    tn.write(b"router ospf 1\n")
    tn.write(b"network 0.0.0.0 255.255.255.255 area 0\n")
    tn.write(b"end\n")
    tn.write(b"write\n")
    tn.write(b"exit\n")

    print(tn.read_all().decode('ascii'))
