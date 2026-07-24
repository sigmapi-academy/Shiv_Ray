count = 0
list6 = [2, 4, 6, 8, 20, 12, 14, 16, 18, 20, 13, 15, 17, 19]
index = 0
while index < len(list6):
    if list6[index] % 3 == 0 or list6[index] % 5 == 0:
        print(list6[index], end = ' ')
        count += 1
    index += 1
print(f'\nnumber of valueindex += 1s divisible by 3 or 5 is {count}')