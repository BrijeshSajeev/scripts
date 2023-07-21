import csv

data=[["Brijesh","CEO",19],["Sherbin","Software Eng",19]]

with open("csv_data.csv",'w') as file:
	writer= csv.writer(file)
	writer.writerows(data)




