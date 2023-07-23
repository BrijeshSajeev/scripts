import csv

data =[{"name":"Brijesh","salary":"200000"},{"name":"Sherbin","salary":"200000"}
,{"name":"Renish","salary":"10000"}]

keys=["name","salary"]

with open("dict.csv",'w') as file:
	writer= csv.DictWriter(file,fieldnames=keys)
	writer.writeheader()
	writer.writerows(data)


