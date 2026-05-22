import random as R
breakHasExecuted = False
skip = R.randint(1, 7)
for i in range(3, 50, skip):
    if i % 3 == 0 and i % 7 == 0: 
        breakHasExecuted = True
        break
    print(i, end=' ')

else:
    print('For loop has exited without executing the break')
if breakHasExecuted:
    print('break has executed')
    
print('skip:', skip)
