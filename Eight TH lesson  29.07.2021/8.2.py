file=open("score.txt","r")#read permission


lines=file.readlines()
for i in lines:


  print(i)

file.close()