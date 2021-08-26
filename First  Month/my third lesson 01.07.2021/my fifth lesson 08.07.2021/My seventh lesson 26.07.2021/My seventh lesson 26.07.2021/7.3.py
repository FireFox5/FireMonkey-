def a_div_b (a,b):
    if b==0:
        print("not ")
        b=1
    c= a / b
    return c


c=a_div_b(a_div_b(a=2,b=1),a_div_b(10,0))
print(c)

d=a_div_b(a=8,b=4)
print( d)