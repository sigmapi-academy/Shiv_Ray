num1 = int(input('Enter dividend: '))
num2 = int(input('Enter divisor: '))

q = num1 // num2
r = num1 % num2
div = num1 / num2

print(f'Quotient: {q}')
print(f'Remainder: {r}')
print(f'Divide: {div:.2f}')

print(f'{num1} + {num2} = {num1 + num2}')
print(f'{num1 ** num2:,}')

print(f'{'test':*>12}')
print(f'{'test':*<12}')
print(f'{'test':*^12}')
price = float(input('Enter your price: '))
print(f'It is very {'Expensive' if price > 50 else 'Cheap'}')
