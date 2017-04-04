colors = ['red', 'blue', 'green', 'orange']

# Concatenation
print(colors + ['purple', 'yellow'])

# Replace a value in a list
cubes = [1, 8, 27, 65, 125]
cubes[3] = 64
print(cubes)
cubes[2:4] = [26, 63]
print(cubes)
cubes[2:4] = []
print(cubes)
cubes[:] = []
print(cubes)

# Add values to a list
cubes.append(216)
cubes.append(7 ** 3)
print(cubes)

# Nesting a list inside a list
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0])
print(x[0][1])
