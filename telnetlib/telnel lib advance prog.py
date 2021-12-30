import datetime
import telnetlib,os
import time,shutil
import wave

Now=datetime.datetime.now()
Date=f"{Now.day}-{Now.month}-{Now.year}-{Now.hour}-{Now.minute}-{Now.second}"
def Main():

    try:
        user=os.environ.get("DB_USER")
        password=os.environ.get("DB_PWD")
        print("i am working")
        time.sleep(3)
        f=open("WTD.txt",'r')
        path=os.mkdir("backup_config")
        print("\nthis code will take backup of all switches\n")
        for line in f:
            HOST=line.strip()
            print(f"\n i am working on {HOST}")
            tn=telnetlib.Telnet(HOST)
            tn.read_until(b"Username: ")
            tn.write(user.encode()+b"\n")

            if password:
                tn.read_until(b"Password: ")
                tn.write(password.encode()+b"\n")

            tn.write(b" terminal len 0\n")
            tn.write(b"sh run\n")
            tn.write(b"exit\n")
            read=tn.read_all().decode()
            path1="backup_config\%s %s.txt"%(HOST,Date)
            with open(path1,'w') as W:
                W.write(read)


            # with open("backup_config\switch %s.txt"%HOST,'w') as Result:
            #     Result.write(read)

        print("I have completed task")
    except FileExistsError:
        print("Config folder is already exist")
        a=input("Press Enter to delete and re run the code")
        if bool(a) is False:
            shutil.rmtree("backup_config") #to remove directory
            print("folder deleted successfully")
            Main()
Main()
open=input("enter [Y/N] to view the config folder: ").upper()
if open=='Y':
    os.startfile("backup_config")
elif open=='N':
    print('Thank you!')
else:
    print('Invalid input')
