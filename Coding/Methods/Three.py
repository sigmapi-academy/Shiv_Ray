def calculate(a, b):
    return a+b, a-b, a*b, a/b, a//b, a**b, a%b

#main code
a = float(input('Enter any number: '))
b = float(input('Enter any number: '))
sum, diff, prod, div, quo, exp, rem = calculate(a, b)
print(f'sum = {sum}')
print(f'difference = {diff}')
print(f'product = {prod}')
print(f'quotient = {quo}')
print(f'exponent = {exp}')
print(f'remainder = {rem}')