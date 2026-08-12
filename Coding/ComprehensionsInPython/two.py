# even_num = []
# for x in range(1,11):
#     if x % 2 == 0:
#         even_num.append(x)
        
# print(even_num)

even_num = [x for x in range(1, 11) if x % 2 == 0]

print(even_num)

odd_num = [x for x in range(1, 11) if x %2 != 0]

print(odd_num)