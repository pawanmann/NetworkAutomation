# Python program to demonstrate working
# of map.

# Return double of n
def addition(n):
	return n + n

# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

#*********************************************************************

#We can also use lambda expressions with map to achieve above result.

# Double all numbers using map and lambda

numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))

#********************************************************

# Add two lists using map and lambda

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))

#By using for loop


# Add two lists using map and lambda

n1 = [1, 2, 3]
n2 = [4, 5, 6]
n3 = []
for i in range(0, len(n1)):
    Result = n1[i] + n2[i]
    n3.append(Result)
print(n3)