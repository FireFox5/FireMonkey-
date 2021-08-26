#magic method

val=50
str_val=str(val)
print(type(str_val))

class parent:
    def __init__(self,last_name):
        self.last_name=last_name
        self.age=2000
    def get_info(self):
        return f"this object:  {self.last_name}-{self.age}"
    def __str__(self):
        return f"this str object:  {self.last_name}-{self.age}"
p1=parent('Naspekov')
print(p1)