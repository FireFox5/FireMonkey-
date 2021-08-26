#Multiple inheritance

class Person:
    name="sam"
    age=30


class Homesapiens:
    generation=2000
    new_era=True

class child(Person,Homesapiens):
    pass

h1=child()
print(h1.name,h1.new_era)



class Mother:
    beauty="precious"
    kindness=True
    def __init__(self):
        print('happy')

class Father:
    height=180
    money=1000000

    def __init__(self,last_name):
        self.last_name=last_name

class Uncle(Father):
    pass
class Child(Father,Mother):
  pass
class grandchild(Child):
 pass

c1=Child('willivanow')
print(c1.last_name,c1.kindness)