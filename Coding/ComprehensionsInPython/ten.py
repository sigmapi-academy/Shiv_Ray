num = [int(x) for x in input("Enter numbers: ").split()]

print(num)

squares = { x * x for x in num}

print(squares)