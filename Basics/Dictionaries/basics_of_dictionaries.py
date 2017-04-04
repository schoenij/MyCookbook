# Building a dictionary
dict_ex = {}
dict_ex['a'] = 'alpha'
dict_ex['g'] = 'gamma'
dict_ex['o'] = 'omega'
print(dict_ex)

# Find the value for each key
print(dict_ex['a'])

# Edit the value that goes with each key
dict_ex['a'] = 'beta'
print(dict_ex['a'])
print(dict_ex)

# Print keys (note order is random)
for key in dict_ex:
    print(key)

# Print the keys and the values in a list
print(dict_ex.keys())
print(dict_ex.values())

for key in sorted(dict_ex.keys()):
    print(key, dict_ex[key])

print(dict_ex.items())

for k, v in dict_ex.items():
    print(k, '>', v)
