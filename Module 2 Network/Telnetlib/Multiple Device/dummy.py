import getpass
import os,shutil
import telnetlib

def Main():
    try:
        user= os.environ.get('DB_USER')
        password=os.environ.get('DB_PWD')

        f=open("WTD.txt",'r')
        path=os.mkdir("Config")
        print("\n This will save the configuration\n")
        for i in f:
            HOST=i.strip()

            print(f"I am working on Router#{HOST} device now")

            tn=telnetlib.Telnet(HOST)
            tn.read_until(b"Username: ")
            tn.write(user.encode()+b"\n")

            if password:
                tn.read_until(b"Password: ")
                tn.write(password.encode()+b"\n")

            tn.write(b"terminal length 0\n")
            tn.write(b"sh run\n")
            tn.write(b"exit\n")
            read=tn.read_all().decode()
            with open("Config\Switch_%s"%HOST,'w') as W:
                W.write(read)
        print("I have done with your task")

    except FileExistsError:
        shutil.rmtree("Config")
        print("Folder Deleted")
        Main()

Main()











