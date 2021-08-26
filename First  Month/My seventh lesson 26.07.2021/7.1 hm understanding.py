import datetime
import tarfile

plane = [
    ["*", "*", "*"],  # 0
    ["*", "*", "*"],  # 1
    ["*", "*", "*"]   # 2
]


def print_plane(plane):
    for i in plane:
        print(f"{i[0]} | {i[1]} | {i[2]}")


def check_winner(plane):
    for i in range(3):
     if plane[i][0]!="*" and plane[i][0]==plane[i][1]==plane[i][2]:
             return plane[i][0]
     for i in range (3):
         if plane[0][i] !="*"and plane[0][i] == plane[1][i]==plane[2][i]:
             return plane[0][i]
     for i in range (3):
         if plane [0][0]!="*" and plane[0][0]==plane[1][1]==plane[2][2]:
             return plane[0][0]
         if plane [0][2]!="*" and plane [0][2]==plane[1][1]==plane[2][0]:
             return plane [0][2]

         return None

   # if plane [1][0]==plane[1][1]==plane[1][2]:
def main():
    print_plane(plane)

    for i in range(9):
        if i % 2 == 0:
            player = "X"
        else:
            player = "0"

        player_x = int(input())
        player_y = int(input())
        plane[player_x][player_y] = player
        winner=  check_winner (plane)
        if winner :
            print()
            print(f"winner is {winner}!!!!!!")
            return
        print(winner)
        print_plane(plane)


main()
def write_to_file(text):
    file = open("results.txt", "a+")
    file.write(text)
    file.close()


def read_from_file():
    file = open("results.txt")
    lines = file.readlines()
    file.close()

    return lines


def main1():
    while True:
        print("1) Вывести счет")
        print("2) Добавить новый счет")
        option = int(input("Выберите вариант! "))
        if option == 1:
            scores = read_from_file()
            for i in scores:
                print(i)
        if option == 2:
            winner1 = input("введите победителя!")
            date = datetime.datetime.now()
            date: date


            write_to_file(f"{winner1}{date}\n")


main1()