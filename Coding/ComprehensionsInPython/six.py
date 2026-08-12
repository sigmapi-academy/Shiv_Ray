import random
num = [x*random.randint(1,10) for x in range(1, 11)]
num_str = [str(x) for x in num]
print(num)
print(num_str)