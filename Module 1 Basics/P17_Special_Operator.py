fruits = ["apple", "banana", "cherry"]

#Membership operator
print("apple" in fruits )
print("Orange" not in fruits )

#Identity Operator
a=[1,2,3,4]
b=[1,2,3,4]
c=(2,2,3)
d=(2,2,3)
e=5
f=5

# print(id(a))
# print(id(b))
# d=(3,3,2)
# print(id(c))
# print(id(d))
print(c is d) #It will check on the basis of Id's(ID is equal to b or not)
print(a is b)