N = int(input('Enter any positive integer values greater than 1: '))
if(N <= 1):
    print('Invalid imput')
else:
    factor = 2
    print(1,end=', ')
    while factor <= N//2:
        if N % factor == 0:
            print(factor,end=', ')
        factor+=1
    print(N)
            
