Works=[]
while True:
    print("1)Add work")
    print("2)Show work")
    option=int(input())

    if option==1 :
        task=input ("put task")
        date_added = input("put date when you add it")
        deadline=input("put deadline for task")
        work=[task,deadline,date_added]
        Works.append(work)
        print("work is added")

    if option==2:
        print("--")
        for i in Works:
            print(i[0],i[2],i[1])
        print("--")