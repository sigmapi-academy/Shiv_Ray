count = 0
list6 = [2, 4, 6, 8, 20, 12, 14, 16, 18, 20, 13, 15, 17, 19]
for e in list6:
    if e % 3 == 0 or e % 5 == 0:
        print(e, end = ' ')
        count += 1
print(f'\nnumber of values divisible by 3 or 5 is {count}')