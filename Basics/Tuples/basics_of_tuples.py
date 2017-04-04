tuple_ex = (1, 2, 'hi')
print(len(tuple_ex))
print(tuple_ex[2])

# Tuples can be assigned corresponding values
(x, y, z) = (1, 33, 'hike')
print(z)

# They can be nested
u = tuple_ex, (5, 3, 'hello')
print(u)

# An empty tuple
empty = ()
print(empty)
print(len(empty))

# A tuple with a single value
singleton = (1, )
print(singleton)
print(len(singleton))
