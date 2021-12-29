# def add(a,b):
#     return a+b

# #print(add(5,6))
# sum(2)

def add(a,*args):
    print(a)
    print(args)
    return a+sum(args)

print(add(2,3))
#
# ## Calling the function
# result = concatenate('hello','hey')
#
# print(result)  # => '' -> empty string

################### For **Kwargs #########################
def dummy(ip,user,pwd):
    print(f'ip: {ip} user:{user} pwd:{pwd}' )

def f1(**kwargs):
    print(kwargs)

f1(ip='192.168.1.1',user='dhiraj',pwd='Sandy')