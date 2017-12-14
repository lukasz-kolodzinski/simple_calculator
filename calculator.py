#Simple calculator

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

def calculator_start():
    answer = input('Type kind of operation: add, subtract, multiply, divide, modulo: ')
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
        else:
            print('Function not supported')
    except:
        print('Operation is not allowed')
