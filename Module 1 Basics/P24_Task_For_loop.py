#Example 1

# l1 = [0, 1, 3, 0, 0,6,7]
# C = len(l1)
# count=0
# for i in range(C):
#     if l1[i] != 0:
#         # here count is incremented
#         l1[count] = l1[i]
#         count += 1
#         print(count)
#
# while count < C:
#         print(count)
#         print(l1[count])
#         l1[count] = 0
#         print(l1)
#         count += 1
# print(l1)


#Example 2
Result=1
def Square(N1,N2):
    Result=pow(N1,N2)
    print("%d raised to the power %d is %d"%(N1,N2,Result))

Num1=input("Enter the integer number:")
Num2=input("Enter the power: ")

Square(int(Num1),int(Num2))
