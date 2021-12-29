import threading
import time
def Range1():
    for i in range(50):
        print("Hi")

def Range2():
    for i in range(50):
        print("Hello")

# Range1()
# Range2()

tn1=threading.Thread(target=Range1)
tn2=threading.Thread(target=Range2)

tn1.start()
time.sleep(0.2)
tn2.start()

tn1.join()
tn2.join()

print("I am the last line")