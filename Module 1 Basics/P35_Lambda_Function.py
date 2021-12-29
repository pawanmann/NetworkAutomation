# Python program to illustrate cube of a number
# showing difference between def() and lambda().


# def cube(y):
#     return y * y * y


#g = lambda x,b: x * b * x * x;print(g(7,8))

cube =lambda x=1,y=0:x+y

print(cube())
