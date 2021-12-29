#1. Simple function


# def CPC():
#     print("I am inside")
#
# print("I am outside")
# CPC()

#2. Passing the variable


def CPC(Company):
    print(Company +" " + "EON Pune")

def Concat(Name,Age=4):
    print("="*30)
    print("Hello %s your age is %s" %(Name,Age))
    print("=" * 30)

C=input ("Enter the name of your company: ")
N=input ("Enter your Name: ")
A= input ("Enter your Age: ")



#Function calling:
CPC(C)
Concat(N,A)

