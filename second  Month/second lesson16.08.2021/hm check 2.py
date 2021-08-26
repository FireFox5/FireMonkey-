current_year=2021
class Person:
    __total_persons=0
    def __init__(self,birth_day,name,**kwargs):
        if birth_day >current_year:
            raise Exception('befijbaefw')
        self.__birth_year = birth_day
        self.__name = name
        self.__language = kwargs.get("language")
        self.increase_total_persons()




    @classmethod
    def get_total_persons(cls):
         return cls.__total_persons

    @ classmethod
    def increase_total_persons(cls):
         cls.__total_persons+-1
    def is_adult(self):
       if current_year-self.__birth_year>=18:
           return True
       else:
           return False

    def get_age(self):
        return current_year-self.__birth_year
    def talk(self):
        print("hello world")
class Teacher(Person):
    def talk(self):
        print('greetings,i am your teacher ')

p1=Person(1995 ,'Jack',language="english")
p2=Person(2000,'Sam',)
p3=Person(2019,'sami',language='russian ')



print(Person.get_total_persons)
print(p2.is_adult(),p3.is_adult(),p1.is_adult())
print(p2.get_age())


t1=Teacher(2002,'ivan')
t1.talk()