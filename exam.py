main_program ={ 'Enter your choice:',
    '1- Add a new employee',
    '2-print all employees',
    '3- delete by age',
    '4- update salary by name',
    '5-end the programe'}
print(main_program)
if input(1):
    print('Enter your choice')
    print(input('name'))
    print(input('age'))
    print(input('salary'))
elif input(2):
    print('Print all employees')
elif input(3):
    print('Delete by age')  
elif input(4):
    print('update salary by name')
elif input(5):
    print([4]) 
else:
     print('invalid choice')  

    #choices        
a= 1
b= 2
c= 3
d= 4
e= 5
for i in main_program:
    print(main_program)