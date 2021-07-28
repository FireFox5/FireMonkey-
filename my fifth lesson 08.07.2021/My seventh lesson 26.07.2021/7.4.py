def int_input():

 while True:
    try:
        age=int(input())
        return age
    except ValueError:
        print("STOP FUCKING MISTYPING ")


age=int_input()
print(age)


raise ValueError


#нужно сделать игру крестики нолики
