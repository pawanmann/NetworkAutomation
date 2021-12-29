# python program to illustrate If statement
#1. if-statement
i = 10
if i > 15:
    print("10 is less than 15")
print("I am Not in if")

#2. If-else
i = 20
if i < 15:
    print("i is smaller than 15")
    print("i'm in if Block")
else:
    print("i is greater than 15")
    print("i'm in else Block")
print("i'm not in if and not in else Block")
################################################################
answer=input("If you want to continue[yes/no]: ").lower()
if answer=='yes':
    print("Let's continue")
elif answer=='no':
    print("No worries, Thank You")
else:
    print("Please enter valid response")

#3. if-else-if
i = 10
if i == 10:
    #  First if statement
    if i < 15:
        print("i is smaller than 15")
    # Nested - if statement
    # Will only be executed if statement above
    # it is true
    if i < 12:
        print("i is smaller than 12 too")
    else:
        print("i is greater than 15")
