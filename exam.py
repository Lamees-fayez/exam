main_program= [
'1) Add new employee',
'2) Print all employees',
'3) Delete by age',
'4) Update salary by name',
'5) End program'
]

print( main_program)
chioce= input()


for i in main_program:
    if chioce == '1':
        print(main_program[0]) ,
        employee_data= {'name'==(input('Enter the name:'),
                        'age'== input('Enter the age:'),
                        'salary'== input('Enter the salary:'))}
        print(main_program)
        chioce= input()
    elif chioce == '2':
         print(main_program[1])
         print(employee_data)
         chioce= input()
    elif chioce == '3':
         print(main_program[2])
         chioce= input()
    elif chioce =='4':
         print(main_program[3])
         chioce= input()
    elif chioce == '5':
        print(main_program[4])
        break
    else :
        print('Invalid input try again.')
    
