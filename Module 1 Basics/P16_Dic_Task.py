Empdb=  {
            1:{"Company":"MP","Team":["NOC","Data Center"]},
            2:{"Company":"SP","Team" :["HR","Accounts"]}
        }
'''
Q1: Enter the new Company "Eon" with Team "IT" and "SD"
Q2: Edit company SP and replace new team with "Funclub" and "CSR"

'''
#Q1
Empdb[3]={"Company":"Eon","Team":["IT","SD"]}
print(Empdb)

#Q2
Empdb[2]["Team"][-1]=["Funclub","CSR"]
# print((Empdb[2]["Cousres"][-1])
print(Empdb)


list1=[1,2,3] 
dict1={'a':1 ,'b':2,'c':3,'d':4}
dod={'x':dict1,'y':{'x':1}}
dol={'y':list1,'x':[5,6,7]}
lod=[dict1,dod,dol]
lol=[[1,2,3],list1,lod]

#Q:Please access 6 of dol

print(dol['x'][1])
print(lol[-1][-1]['x'][1])

print(dol['x'][-2])
print(lol[2][2]['x'][-2])





