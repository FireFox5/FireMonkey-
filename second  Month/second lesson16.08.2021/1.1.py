class robot:
    head:100
    body:200
    arm:2
    leg:2
    CPu:"мощная штучка"
   #docstring
    def __init__(self,cpu_name):
        self.cpu=cpu_name

r1=robot("apple")
r2=robot('puma')
r3=robot('nike')
print(r1.cpu)
print(r1.body)
print(robot.__doc__)



