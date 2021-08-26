import random,os

candidates=["amantur",'atai','sultan','aktan','abai']
r=random.choice(candidates)
print(r)
print(candidates[random.randint(0,4)])


greencard=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]



random.shuffle(greencard)
print(greencard[-1])

this_directory=os.getcwd()
print('PATH',this_directory)
print(os.getlogin())
print(os.listdir())

#new_folder='August'
#path=os.path.join(this_directory,new_folder)
#os.mkdir(path)

import datetime
d=datetime.datetime.now()
print(d)
#=====================================
#from datetime import date, datetime
from random import choice,shuffle
from random import randint as randomize
res= choice(candidates)
shuffle(candidates)
rn=randomize(0,100)
#print(rn)


from datetime import date,datetime
t1=date(year=2017,month=5,day=30)
t2=date(year=2016,month=2,day=15)
diff=t1-t2
print(diff)


