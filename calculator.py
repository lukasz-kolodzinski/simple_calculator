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
    if answer == 'add':
        addition()

