dictionaty={

}
def main ():
    while True:
        word=input()
        if word in dictionaty:
            print(dictionaty[word])
        else :
            print("add new word ")
            option=int(input("choose varint"))
            if option== 1:
                translation=input(f"put the translation of the word{word} ")
                dictionaty[word]=translation
            else:
                pass

        
main()