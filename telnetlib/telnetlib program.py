import telnetlib,os
try:
    user=os.environ.get("DB_USER")
    password=os.environ.get("DB_PWD")
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

        with open("backup_config\switch %s.txt"%HOST,'w') as Result:
            Result.write(read)

    print("I have completed task")
except FileExistsError:
    print("Config folder is already exist")
