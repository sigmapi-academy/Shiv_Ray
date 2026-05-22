# S = 2 - 4 + 6- 8 + … n terms
n = int(input('Enter number of terms: '))
sign = 1
sum = 0
for i in range(1, n):
    d = i*2*sign
    if sign == 1:
        print(d, end = '', sep='')
    else:
        print(d, '+', end = '',sep='')
    sum += d
    sign = sign * (-1)
else: # this else is the part of for loop
    d = n * 2 * sign
    sum += d
    print(d, ' =', sum)
    
