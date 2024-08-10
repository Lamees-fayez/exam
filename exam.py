main_program= { 
'1) Add new employee',
'2) Print all employees',
'3) Delete by age',
'4) Update salary by name',
'5) End program'
}
print( main_program)
a= ('1) Add new employee')
b =('2) Print all employees')
c=('3) Delete by age')
d=('4) Update salary by name')
e=('5) End program')

chioce= input()
for i in main_program:
    if chioce == '1':
        print(a) ,
        employee_data= {'name'==(input('Enter the name:'),
                        'age'== input('Enter the age:'),
                        'salary'== input('Enter the salary:'))}
        print(main_program)
        continue    
    elif chioce == '2':
         print(b)
         print(name , age , salary)
    elif chioce == '3':
         print(c)
    elif chioce =='4':
         print(d)
    elif chioce == '5':
        print('End program')
        break
    else :
        print('Invalid iput try again.')
    
