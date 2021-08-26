name=input()
age=int(input())
hobby=input()

if name=="Aman" and age>=16 and hobby=="swimming":
    print("Hello owner!")
    login=input()
    password=input()
    if login=="Aman" and password=="123":
        print("owner log in")
    else:
        print("your password and logon not correct")

else:
    print("you are not owner")


if name=="Aman" or age>=16 or hobby=="swimming":
    print("you are aman or you age is 16 or you like swimming")
else:
    print("you are not owner")


