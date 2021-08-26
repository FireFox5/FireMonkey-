import datetime
todo=[]
try:
    while True:
        print()
        opera=int(input("add work(1)?-or show(2)"))
        print()


        if opera == 1:
            todo=input("put task")
            date=datetime.datetime.now()
            todo.append({
                'todo':todo,
                'date':date
            })
            print("task added!")
            print()
        elif opera ==2:
            for todo in todo:
                print()
                print(f'task:'{todo["todo"]}\nдата создания:{todo[""]})
except ValueError:
    print('put tekst')
except:
    print('error')
