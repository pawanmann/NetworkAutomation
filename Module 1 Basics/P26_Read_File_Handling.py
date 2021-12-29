Emp_file=open("employee1.txt",'r')
#emp_file=open("employee1.txt",'r')
# print(Emp_file.readline())
#print(Emp_file.readline())
#print(Emp_file.readlines())
#print(Emp_file.read()) #It will fetch all the line in file

# print(emp_file.readline())#It will read line by line
# print(emp_file.readline())
print(Emp_file.read().splitlines())
# A=Emp_file.readlines()# All the data in list format
#
# for emp in A:
#     print(emp)

Emp_file.close()







