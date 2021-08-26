
#def hello(arg1, arg2,*arg3):
 #       print("hello HOw are you", arg1)
  #      print("you first and second name are registred", arg2)
   #     print(arg3)

#hello("sultan", "naspekov","second fuck day","i hope you are good")

#def make_sum(a,b,*args,**kwargs):
 #       print(kwargs)
  #      print(kwargs["name"])
   #     sum=0
    #    for i in args:
     #           sum+=1
      #  return a+b+sum
#x=make_sum(2,5,1,1,1,1,1,1,name=125)
#print(x)

class house:
        wigth=300
        heigh=150
        price=2000
        doors=12
        rooms=21
        def __init__(self,address):
                self.address=address


my_house=house("stepanenko23")
house2=house("stepanenko43")
#print(my_house.wigth, my_house.rooms,my_house.address)
#print(house2.wigth,house.rooms,house2.address)

class user:
        website='gmail'
        domain='kg'

        def __init__(self,name,last_name,login,password):
                self.name=name
                self.last_name=last_name
                self.login=login
                self.password=password
        def say_hello(self):
                print('hello world',self.name )
        def get_login(self):
                print("your login is ",self.login)
        def change_login(self,new_login):
                self.login=new_login
        def get_passport(self):
                print("your password is",self.password)
        def change_password(self,new_pass):
                if len(new_pass)<4:
                        raise Exception('Password over 4 letters')
                self.password=new_pass
        def change_website(cls,new_website):
                cls.website=new_website

v1=user('suli','white','*-*-*-','123')
v2=user('wuli','black','1212','5434')
v3=user("adilet",'kamtemirow','4545','9514')

v1.get_login()
v1.change_login("my name is sultan ")
v1.get_login()
v2.get_passport()
v2.change_password("Naspekov")
v2.get_passport()

#print(v1.name,v2.name,v3.name)
#v1.say_hello()
#v2.say_hello()
#v3.say_hello()
#v2.get_login()

print(v1.password)
v1.change_password('super_puper')
print(v1.password)


v1.change_website('yuutube')
print(v1.website)