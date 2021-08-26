
def write_to_file(text):
    file = open("scor.txt", "a+")
    file.write(text)
    file.close()


def read_from_file():
    file = open("scor.txt")
    lines = file.readlines()
    file.close()

    return lines


def main():
    while True:
        print("1) Вывести счеты комманд")
        print("2) Добавить новый счет")
        option = int(input("Выберите вариант! "))
        if option == 1:
            scores = read_from_file()
            for i in scores:
                print(i)
        if option == 2:
            commands = input()
            score = input()
            write_to_file(f"{commands}-{score}\n")


main()
