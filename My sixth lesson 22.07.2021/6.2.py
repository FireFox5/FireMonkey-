import random

def a_plus_b (a,b,c):

    print(a+b*c)


#a_plus_b(2,2,2)
#a_plus_b(4,4,4)
#a_plus_b(8,8,8)

def pojalet_temirlan ():
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    result=int (input(f"угадай results этих чисел {num2}*{num1}"))
    if result ==num1*num2:
        print("oookkkkkkeeey")
    elif result-5000<= num1*num2 <= result+5000:
        print("было близко")
    else:
        print("sorry not your day")


def kickplayer(name):
    if name =='temirlan':
        pojalet_temirlan()
    else:
        print(f"{name}you in ")

def main():
    for i in range(3):
        name=input("put your name ")
        kickplayer(name)
main()


#сделать игру угадай число должно быть ьаин и сколько раундов играть и было число чтоб рядом быть около 5  числа и главное угадать число