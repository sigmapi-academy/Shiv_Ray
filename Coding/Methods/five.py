x = 500
def f1():
    global x
    x = 100
    print(f'Global x = {x}')
    x += 20
    print(f'Global x = {x}')
    
    
#main code
f1()
x += 10
print(f'Global x = {x}')
