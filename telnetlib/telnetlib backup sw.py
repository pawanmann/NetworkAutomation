import telnetlib
import os

# HOST="192.168.75.100"
# HOST="192.168.75.10"

# user = "pawan"
# password = "cisco"

# user = input("Enter the telnet username: ")
# password = input("Enter the telnet password: ")

user=os.environ.get('DB_USER')
password = os.environ.get('DB_PWD')
file=open("WTD.txt")
for HOST in file:
    HOST=HOST.strip()


    tn=telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') +b"\n")


    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') +b"\n")
    print("*"*30 + " Welcome to Automation "+ "*"*30)
    print(f"i am inside {HOST}")

        # path=os.mkdir("../config")
    # print(f"this code will save configuration of {HOST}")




    tn.write(b"terminal length 0\n")
    tn.write(b"sh run\n")
    tn.write(b"exit\n")

print(tn.read_all().decode())
#Result = tn.read_all().decode()

# with open(f"Config\Switch %s.txt"%HOST,'w') as Output:
#     Output.write(Result)
# print(Result[0:5])
# print(Result)
print(" completed task!!!!!!!")