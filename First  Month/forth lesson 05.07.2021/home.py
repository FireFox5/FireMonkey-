Works=[]
while True:
    print("1(Add work")
    print("2(show list ")
    option=int(input())


    if option==1:
         task=input("add work ")
         date_the_work_add=input("put date ")
         deadline=input("deadline")
         work=[task,date_the_work_add,deadline]
         Works.append(work)
         print("work is added")


    if option==2:
         print("---------")
         for i in Works:
          print(i[0],i[1],[2])
         print("-----------")