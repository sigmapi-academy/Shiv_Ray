def square(x):
    return x * x

num = [x for x in range(1,11)]
res = [square(x) for x in num]
print(num)
print(res)