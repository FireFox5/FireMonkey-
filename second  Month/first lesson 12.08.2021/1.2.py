#class house:
 #   width:300
 #   height:150
 #   price:2000
  #  romms:6
  #
#def __init__(self,adress):
 #   self.adress=adress



#my_house= house("stepanenko23")
#house2: house=house("jal23")

#print(my_house.width,my_house.romms,my_house.adress)
#print(house2.width,house2.romms,house2.adress)
class User:
    '''this class describes the behavior of users '''

    website="gmail"
    doamin="kg"

    def __init__(self,name,last_name,login,password):
        self.name="jack"
        self.last_name="name"
        self.login="simple"
        self.password="1213"

    def say_hello(self):
        print("hello world",self.name)

    def get_login(self):
        print("your login is",self.login)

v1=User("akgm","wgf","fgggr","213123")
v2=User("11111","22222","33333",'12332')
v3=User("ivan","vasua","affe","esgsg")


v1.say_hello()
v2.say_hello()
v3.say_hello()


v2.get_login()
print(v1.website,v2.website,v3.website)
#