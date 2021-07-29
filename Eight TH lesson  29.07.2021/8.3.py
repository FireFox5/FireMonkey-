def write_tofile(text):
    file=open("score2.txt" ,"a+" )
    file.write(text)
    file.close()

def read_fromit():
    file=open("score2.txt")
    lines=file.readline()
    file.close()

    return lines

def main():
    print("1)Output the score of the teams ")
    print("2)Add new score")
    option=int(input("choose variant"))
    if option ==1:
        scores=read_fromit()
        for i in scores:
            print(i)
        if option==2:
            commands=input()
            score=input()
            write_tofile(f"{commands}{score}\n")

main()
