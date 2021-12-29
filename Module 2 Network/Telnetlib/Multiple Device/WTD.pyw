import sys,getpass,os,shutil
import telnetlib,time
import tkinter as tk
from tkinter import *
from tkinter import messagebox

def Main():
    try:
        user =User.get()
        password=Pwd.get()
        time.sleep(2)
        f=open("WTD.txt",'r')
        path=os.mkdir("Config")

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

            W=open("Config\Switch %s.txt"%HOST,'w' )
            W.write(read)
            W.close()

        messagebox.showinfo("Sucess", "Backup Done")
        os.startfile("Config")

    except FileExistsError:
        messagebox.showinfo("Error", "Existing Config folder deleted")
        shutil.rmtree("Config")
        print("Folder deleted successfully")
        Main()

master=Tk()
master.title('Backup Config')
master.geometry('250x70')

r0=2

Label(master, text="Username").grid(row=r0,column=0)
User =Entry(master)
User.grid(row=r0, column=2)

r1=r0+2
Label(master, text="Password").grid(row=r1,column=0)
Pwd =Entry(master,show='*')
Pwd.grid(row=r1, column=2)

r2=r1+2

Button(master, text='Login', command=Main,bg="lightBlue").grid(row=r2, column=2)







