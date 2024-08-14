main_program= [
'1) Add new employee',
'2) Print all employees',
'3) Delete by age',
'4) Update salary by name',
'5) End program'
]
employees=[]
while True:
    print(main_program)
    chioce= input()
    if chioce == '1':
        print(main_program[0]) ,
        name = (input('Enter employee name :    ').strip().capitalize() )
        age= int (input('Enter employee age :     ').strip())
        salary= int(input('Enter employee salary :     ').strip())
        employees.append({'name': name ,
         'age':age ,
          'salary': salary})
        print('employee Added')
        print(employees)
    elif chioce == '2':
        print(main_program[1])
        print('Employees list:')
        for emp in employees:
            print(f"Employee name {emp['name']} his age is {emp['age']} his salary is {emp['salary']}")

    elif chioce == '3':
        print(main_program[2])
        age_from= int(input('Enter age from : ').strip())
        age_to= int(input('Enter age to : ').strip())
        for i in range (age_from , age_to+1):
            for emp in employees :
                print(f"Deleting {emp['name']}")
                employees.remove(emp)

    elif chioce =='4':
        print(main_program[3])
        name= (input('Enter employee name:').capitalize().strip())
        new_salary=int(input('Enter new salary'))
        for emp in employees:
            if emp ['name']== name:
                emp['salary']== new_salary
                print(f'Employee {emp["name"]} updated' ) 
            else:
                print('Employee not found')
    elif chioce == '5':
        
        print('**End program**')
        break
    else :
        print('Invalid input try again.')
    
