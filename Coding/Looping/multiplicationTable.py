# 5 10, 15, 20, ..., 50
# 6, 12, 18, ... 60
# ...
# ...
# n, 2n, 3n,... 10n

m = int(input('Enter the start number: '))
n = int(input('Enter the end number: '))
t = int(input('Enter number of times for each table: '))
print('-'*70)
print('\tMultiplication table from',m, 'to', n, 'upto', t, 'times')
print('-'*70)
while m <= n:
    for i in range(1, t):
        p = m * i
        print(p, end = ', ')
    else:
        print(m*t) #print the last value and end the line
    m += 1
print('-'*70)