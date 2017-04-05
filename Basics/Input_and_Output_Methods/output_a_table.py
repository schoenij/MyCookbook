# Example of str.rjust()
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), repr(x*x*x).rjust(4))

# Example of str.ljust()
for x in range(1, 11):
    print(repr(x).ljust(2), repr(x*x).ljust(3), repr(x*x*x).ljust(4))

# Example of str.center()
for x in range(1, 11):
    print(repr(x).center(2), repr(x*x).center(3), repr(x*x*x).center(4))

# Can also use this method
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print('{0:10} ==> {1:10d}'.format(name, phone))
