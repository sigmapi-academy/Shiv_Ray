msg = 'Hello! Python'
def f1():
    x = 100
    print(x)
    x += 20
    print(x)
    print(f'from f1(): {msg}')
    
#main code
f1()
# x += 10
print(f'From main: {msg}')
