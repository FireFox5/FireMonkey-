import re

something = open("src/data_corey.txt", 'r')
line_count = 0
line_numbers = 0
kak=0
for line in something:

    if line != "\n":


        kak += 1
        if (kak == 2):
            if (line.find('7', 11, 12) == 11):
                line_numbers += 1
        if (kak == 4):
            kak = 0
            line_count += 1


something.close()
print(line_count)
print(line_numbers)
