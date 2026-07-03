def add(a, b):
    return a + b

def subtract(a, b):
    return (a - b)

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return 'Divisible by zero is not allowed'
    else:
        return a / b

def remainder(a, b):
    if b == 0:
        return 'Divisible by zero is not allowed'
    else:
        return a % b

def inputValue():
    global a, b
    a = int(input('Enter first number: '))
    b = int(input('Enter second number: '))

 
#main code
a = 0
b = 0
while True:
    print('=====Basic Calculator======')
    op = input('Enter any arithmetic operator (+,-,*,/,%,x(exit)): ')
    
    match op:
        case '+': 
            inputValue()
            sum = add(a,b)
            print(f'sum = {sum}')
        case '-': 
            inputValue()
            diff = subtract(a,b)
            print(f'difference = {diff}')
        case '*':
            inputValue()
            prod = multiply(a, b)
            print(f'Product = {prod}')
        case '/':
            inputValue()
            div = divide(a,b)
            print(f'Quotient = {div}')
        case '%':
            inputValue()
            rem = remainder(a, b)
            print(f'Remainder = {rem}')
        case 'x' | 'X': 
            print('Good bye')
            exit()
        case _:
            print('Wrong option is selected')
        
            
            
            
            