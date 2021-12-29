# Initiating Dic
data={ 'Name': 'Dhiraj',
       'Emp_ID':5,
       'Addr':'pune'
       }

#Accessing Dic:
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print("dict['Name']: "), dict['Name']
print("dict['Age']: "), dict['Age']

#Updating Dic
# data['call']='123456'
#data['Details']='7350'
#Functions

print(data)
print(data['Emp_ID'])
#print(data.keys())
#print(data.values())
#print(data.items()) #Read only
#print("Emp_id" in data) #will return Boolean & only for key
#data.pop("Name")
print(data)
#del(data)
print(data)

'''
list1=[1,2,3] 
dict1={'a':1 ,'b':2,'c':3,'d':4}
Dist of dict : dod={'x':dict1,'y':{'x':1}}
Dict of list : dol={'y':list1,'x':[5,6,7]}
list of dict : lod=[dict1,dod,dol]
list of list : lol=[[1,2,3],list1,lod]

'''



l1=[1,2,3]
dict1={'a':1 ,'b':2,'c':3,'d':4}
dod={'ip':'10.10.10.1','data':dict1}
dol={'x':l1,'y':[8,9,10]}
lod=[dict1,dod,dol]
lol=[[1,2,3],l1,lod]

print(lol[2][0]['c'])
