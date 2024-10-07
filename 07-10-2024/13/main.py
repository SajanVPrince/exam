from add import *
from sub import *
from mul import *
from div import *

while True:
    print('''
    1.add
    2.sub
    3.mul
    4.div
    5.exit''')
    c=int(input('enter your choice : '))
    if c==1:
        add()
    elif c==2:
        sub()
    elif c==3:
        mul()
    elif c==4:
        div()
    elif c==5:
        break
    else:
        print('invalid choice')