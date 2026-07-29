# Program to increment the elements of a list.
# The list is passed as an argument to the function and increment value also.

def increment(li1, incr):
    for i in range(len(li1)):
        li1[i] += incr

#main code
list1 = [10, 20, 30, 40, 50]

print(f'list before method call: {list1}')
i = int(input('Enter the increment value: '))
increment(list1, i)
print(f'list after method call: {list1}')
