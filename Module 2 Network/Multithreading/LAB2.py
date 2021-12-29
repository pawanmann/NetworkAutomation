import threading,time

start=time.time()

def Cube(numbers):
    time.sleep(2)
    for i in numbers:
        print(i*i*i)

def Square(numbers):
    time.sleep(2)
    for i in numbers:
        print(i*i)

numbers=[2,3,4,9]
#
tn1=threading.Thread(target=Square,args=(numbers,))
tn2=threading.Thread(target=Cube,args=(numbers,))

tn1.start()
time.sleep(0.2)
tn2.start()

tn1.join()
tn2.join()
#
# Square(numbers)
# Cube(numbers)

#print("HI")

end=time.time()

print(end-start)