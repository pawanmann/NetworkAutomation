                                        #Break
# Python program to
# demonstrate break statement

s = 'geeksforgeeks'
# Using for loop
for letter in s:

	print(letter)
	# break the loop as soon it sees 'e'
	# or 's'
	if letter == 'e' or letter == 's':
		break

print("Out of for loop")
print()

i = 0

# Using while loop
while True:
	print(s[i])

	# break the loop as soon it sees 'e'
	# or 's'
	if s[i] == 'e' or s[i] == 's':
		break
	i += 1

print("Out of while loop")

#***************************************************************************************************

                                            #Continue

#1

# i = 1
# while i < 6:
#     i += 1
#     if (i == 3):
#         continue
#     print(i)

#2.

fruits=["apple","banana","cherry"]
for x in fruits:
    if x=="banana":
        continue
    print(x)

                                        #Pass

a = 10
b = 20

if(a<b):
    pass
else:
    print("b<a")

