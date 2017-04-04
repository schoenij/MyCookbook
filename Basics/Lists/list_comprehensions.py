nums = [1, 2, 3, 4]
squares = [n*n for n in nums]
print(squares)

strings = ['hello', 'and', 'goodbye']
caps = [n.upper() + "!!!" for n in strings]
print(caps)

fruits = ['apple', 'cherry', 'banana', 'lemon']
afruits = [s.upper() for s in fruits if 'a' in s]
print(afruits)

nums = [2, 8, 1, 6]
small = [n for n in nums if n <= 2]
print(small)