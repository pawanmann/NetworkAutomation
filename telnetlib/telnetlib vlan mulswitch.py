import telnetlib
import os

# HOST="192.168.75.100"
HOST="192.168.75.10"

# user = "pawan"
# password = "cisco"

# user = input("Enter the telnet username: ")
# password = input("Enter the telnet password: ")

user=os.environ.get('DB_USER')
password = os.environ.get('DB_PWD')

for a in range(10,12):
    HOST="192.168.75."+str(a)
    print(HOST)
    tn=telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') +b"\n")


    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') +b"\n")
    print("*"*30 + " Welcome to Automation "+ "*"*30)
    print(f"i am inside {HOST}")

    # path=os.mkdir("../config")
    print(f"this code will save configuration of {HOST}")




    tn.write(b"conf t\n")


# tn.write(b"vlan 10\n")
# tn.write(b"name admin\n")
# tn.write(b"vlan 20\n")
# tn.write(b"name sales\n")
# tn.write(b"vlan 30\n")
# tn.write(b"name IT\n")


    for i in range (2,30):
        tn.write(b"vlan %s\n"%str(i).encode())
        tn.write(b"name Python_%s\n"%str(i).encode())
    tn.write(b"end\n")
    tn.write(b"wr me\n")
    tn.write(b"sh vl brief\n")
    tn.write(b"exit\n")

print(tn.read_all().decode())
#Result = tn.read_all().decode()

# with open(f"Config\Switch %s.txt"%HOST,'w') as Output:
#     Output.write(Result)
# print(Result[0:5])
# print(Result)
print(" completed task!!!!!!!")