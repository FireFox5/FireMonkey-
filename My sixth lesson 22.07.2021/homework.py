import random

def game_start():
    simple_number=random.randint(1,10)
    results=int(input({"The number from 1 to 10"}))

    if results==simple_number:
        print("-------you are win -------")
    elif results-5<=simple_number<=results+5:
        print("-------было близко------- ")
    else:
        print("-------ТЫ не угадал-------  ")

def game_number (game_number):
    if game_number == "1":
        game_start()
    else:
        print("-------write down number 1------- ")

def main():
    for i in range(int(input("-------how many times do you wanna play?-------"))):
        number = input("--------For starting the game write down1-------- ")
        game_number(number)



main()