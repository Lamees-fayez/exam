a = ('1) Add new employee')
b = ('2) Print all employees')
c = ('3) Delete by age')
d = ('4) Update salary by name')
e = ('5) End program')
print( a ,b ,c ,d ,e)
chioce= input()
while True:
    if chioce == '1':
        print(a)
    elif chioce == '2':
        print(b)
    elif chioce == '3':
        print(c)
    elif chioce =='4':
        print(d)
    elif chioce == '5':
        break 
    else:
        print('Invalid iput try again.')
