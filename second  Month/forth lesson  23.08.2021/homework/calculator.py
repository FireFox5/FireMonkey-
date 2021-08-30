from certifi.__main__ import args


class calculator:
    # x = int(input("введите дополнительное число"))
    def plus(self,a,b,*args):
        z=int(input("put number"))
        for num in args :
            z+=num
        print(a,"+",b,'+',z,"=",a+b+z)
    def minus(self,a,b, *args):
        z=int(input("put number"))
        for num in args :
            z-=num
        print(a, "-", b,'-',z ,"=", a - b-z)
    def multiply(self,a,b,*args):
        z=int(input("put number"))
        for num in args :
            z*=num
        print(a, "*", b,'*',z,"=", a * b*z)
    def divide(self,a,b,*args):
        z=int(input("put number"))
        for num in args :
            z/=num
        print(a, "/", b,'/',z, "=", a / b/z)




