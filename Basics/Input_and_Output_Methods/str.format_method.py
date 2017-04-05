# Basic usage of str.format()
print('We are the {} who say "{}!"'.format('knights', 'Ni'))

# Number in brackets can refer to the position of the output
print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))

# Using keyword arguments in str.format()
print('This {food} is {adjective}.'.format(
    food='spam', adjective='absolutely horrible'))

# Combining numbers and keywords
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
                                                   other='Georg'))

contents = 'eels'
print('My hovercraft is full of {}.'.format(contents))
print('My hovercraft is full of {!r}.'.format(contents))

import math
print('The value of Pi is approximately {}.'.format(math.pi))
