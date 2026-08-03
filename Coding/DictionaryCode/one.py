# Q: Create a dictionary of. Odd numbers between one and 10.
# Where the key is the decimal number and the value is the
# corresponding number in words. Perform the following 
# operations on this dictionary:
# 			i. Display the keys.
# 			ii. Display the values.
# 			iii. Display the items.
# 			iv. Find the length of the dictionary.
# 			v. Check if 7 is present or not.
# 			vi. Check if two is present or not.
# 			vii. Retrieve the value corresponding to the key 9.
#          viii. Delete the item from the dictionary corresponding to key 9.

ODD = {1 : 'One', 3 : 'Three', 5 : 'Five', 7 : 'Seven', 9 : 'Nine'}
print(ODD)
print(f'Keys: {ODD.keys()}')
print(f'Values: {ODD.values()}')
print(f'Items: {ODD.items()}')
print(f'Number of items: {len(ODD)}')
print(f'Is 7 present: {7 in ODD}')
print(f'Is 2 present: {2 in ODD}')
print(f'9 : {ODD[9]}')
del ODD[9]
print(f'After deletion: {ODD}')
