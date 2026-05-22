import random as R
breakHasExecuted = False
skip = R.randint(1, 7)
count = 0
for i in range(3, 50, skip):
    if i % 3 == 0 and i % 7 == 0: 
        continue
    
    print(i, end=' ')
    count += 1
    if count % 10 == 0:
        print()
else:
    print('\nFor loop has exited')
    
print('skip:', skip)
