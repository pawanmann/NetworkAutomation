import os,shutil
import telnetlib,time

def Main():
    try:
        user =os.environ.get("DB_User")
        password=os.environ.get("DB_PWD")
        print("I am working......")
        time.sleep(2)
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
        a=input("Press enter key to delete and rerun the program:" )
        if bool(a) is not True:
            shutil.rmtree("Config")
            print("Folder deleted successfully")
            Main()

Main()
Open=input("Press any key to view Config Folder(Y/N): ").upper()
if Open=='Y':
    os.startfile("Config")
elif Open=='N':
    print("Thank YOU!!!")
else:
    print("Please enter valid input")






