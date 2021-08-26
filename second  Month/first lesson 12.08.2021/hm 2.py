class Employee:
    emp_count = 2
    work_rate = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_count(self):
        pass

    def display_employee(self):
        print('My name is', self.name,'And my salary is ',self.salary)
    def change_name(self,new_name ):
        self.name=new_name
    def get_total_salary(self):
        print('total salary ',self.salary)


p1 = Employee('bakai','250$')
p2 = Employee('Danchik','300$')
"====================================="
p1.display_employee()
p1.change_name("Abai")
p1.display_employee()
p1.get_total_salary()