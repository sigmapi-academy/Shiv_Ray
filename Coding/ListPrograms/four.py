# Program to increment the elements of a list.
# The list is passed as an argument to the function and increment value also.

def increment(li1, incr):
    li2 = list(li1) #local copy created
    for i in range(len(li2)):
        li2[i] += incr
    print(f'list inside method call: {li2}')    
    

#main code
list1 = [10, 20, 30, 40, 50]

print(f'list before method call: {list1}')
i = int(input('Enter the increment value: '))
increment(list1, i)
print(f'list after method call: {list1}')
