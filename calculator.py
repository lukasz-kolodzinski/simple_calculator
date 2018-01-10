#Simple calculator. Project created to refresh python's basics.

def addition():
    a = int(input('Type first number '))
    b = int(input('Type second number '))
    print(a + b)

def subtraction():
    a = int(input('Type first number '))
    b = int(input('Type second number '))
    print(a - b)

def multiplication():
    a = int(input('Type first number '))
    b = int(input('Type second number '))
    print(a * b)

def division():
    a = int(input('Type first number '))
    b = int(input('Type second number '))
    print(a / b)

def modulo():
    a = int(input('Type first number '))
    b = int(input('Type second number '))
    print(a % b)

def count_to_ten():
    for i in range (1, 11):
        print(i)

calculator_on = 1

def quit():
    global calculator_on
    calculator_on = 0    

def calculator_start():
    answer = input('Type kind of operation: add, subtract, multiply, divide, modulo, count to 10 or quit: ')
    try:
        if answer == 'add':
            addition()
        elif answer == 'subtract':
            subtraction()
        elif answer == 'multiply':
            multiplication()
        elif answer == 'divide':
            division()
        elif answer == 'modulo':
            modulo()
        elif answer == 'count to 10':
            count_to_ten()
        else:
            quit()
    except:
        print('Operation is not allowed')

while calculator_on == 1:
    calculator_start()
