# Sets are unordered collections with no duplicates
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

if 'orange' in basket:
    print("True")
else:
    print("False")

if 'crab apple' in basket:
    print("True")
else:
    print("False")

# Can use {} or set() to indicate a set
a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
print(a - b)    # Shows letters in a but not b
print(a | b)    # Shows letters in either a or b
print(a & b)    # Shows letters in both a and b
print(a ^ b)    # Shows letters in a or b but not both

# Set comprehensions
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
