import datetime
today=datetime.date.today()
file=open("pupil.txt","w")


file.write("hello word? \n")
file.write ("i love python? ")
data=datetime.datetime.now()

file.close()
