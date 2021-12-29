#Example 1
# try:
#   print(x)
# except:
#   print("An exception occurred")

#Example 2
# try:
#   print(x)
# except NameError:
#   print("Variable x is not defined")
# except:
#   print("Something else went wrong")

#Example 3
# try:
#   print("Hello")
# except:
#   print("Something went wrong")
# else:
#   print("Nothing went wrong")

#Example 4

try:
  print(x)
except:
    print("Something went wrong")
finally:
  print("The 'try except' is finished")

print("Hi")
#***********************************

# try:
#     age=int(input('Enter your age: ')) #give input as string "a"
# except:
#     print ('You have entered an invalid value.')
# else:
#     if age <= 21:
#         print('You are not allowed to enter, you are too young.')
#     else:
#         print('Welcome, you are old enough.')
#
