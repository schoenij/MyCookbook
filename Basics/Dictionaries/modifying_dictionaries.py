# Dictionary formatting
hash = {}
hash['word'] = 'garfield'
hash['count'] = 42
s = 'I want %(count)d copies of %(word)s' % hash    # %d is used for integers and %s is used for strings
print(s)

# Using the 'del' operator
dict = {'a': 1, 'b': 2, 'c': 3}
print(dict)
del dict['b']
print(dict)
