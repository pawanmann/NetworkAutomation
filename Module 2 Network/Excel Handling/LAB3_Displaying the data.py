import pandas

filename="Sample.xlsx"
Read= pandas.read_excel(filename)
df=pandas.DataFrame(Read,columns=['IP Address'])
print(Read.fillna(0))