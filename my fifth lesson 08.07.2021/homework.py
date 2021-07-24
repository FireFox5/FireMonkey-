def start():
    print('choose one of the options: ')
    print('1 – Add new word')
    print('2 – Translate word')
    print('3 – Change the meaning of the word')
    print('4 – Delete word')
    print('5 - Show how many words')
    print('0 – Exit')
    return


dictionary = dict()
while True:
    start()
    n = int(input('choose one of the options: '))
    if n == 1:
        word = input('put the word: \n')
        tran = input('put the  translation of the word: \n')
        dictionary[word] = tran
    elif n == 2:
        word = input('put word: \n')
        if word in dictionary:
            print(word, '->', dictionary[word])
        else:
            print('No words in dictionary like that ')
    elif n == 3:
        word = input('put the word that need to change: \n')
        tran = input('put the translation: \n')
        dictionary[word] = tran
    elif n == 4:
        word = input('put the word that need to change: \n')
        if word in dictionary:
            dictionary.pop(word)
        else:
            print('No words in dictionary like that')
    elif n == 5:
        print(*dictionary.keys(), sep='\n')
    else:
        break