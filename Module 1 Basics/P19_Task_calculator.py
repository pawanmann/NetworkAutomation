def Add(N1, N2):
    N3 = int(N1) + int(N2)
    print("Addition of %d and %d is %d" % (N1, N2, N3))


def Sub(N1, N2):
    N3 = int(N1) - int(N2)
    print("Substraction of %d and %d is %d" % (N1, N2, N3))


def Div(N1, N2):
    N3 = int(N1) / int(N2)
    print("Division of %d and %d is %d" % (N1, N2, N3))


def Mul(N1, N2):
    N3 = int(N1) * int(N2)
    print("Multiplication of %d and %d is %d" % (N1, N2, N3))


def Input():
    global Oper, Num1, Num2
    print("\n" + "=" * 4 + "Welcome to CC Calulator" + "=" * 4 + "\n")
    Num1 = input("Enter 1st integer number: ")
    Num2 = input("Enter 2nd integer number: ")
    Oper = input("Enter the operation(+,-,/,*): ")
    Rep()


def Rep():
    if Oper == "+":
        Add(int(Num1), int(Num2))
    elif Oper == "-":
        Sub(int(Num1), int(Num2))
    elif Oper == "/":
        Div(int(Num1), int(Num2))
    elif Oper == "*":
        Mul(int(Num1), int(Num2))
    else:
        print("Please enter valid operator from the list")
    Agn = input("Press any key to continue")
    if bool(Agn) is not True:
        Input()

Input()
