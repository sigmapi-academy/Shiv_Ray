start = int(input('Enter start value: '))
end = int(input('Enter end value: '))
sv = int(input('Enter skip or Jump: '))
for i in range(start, end+1, sv):
    print(i, end=' ')
    
print('\nReverse: ')
for i in range(end, start-1, -sv):
    print(i, end = ' ')