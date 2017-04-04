# First in, first out
import collections
queue = collections.deque(['Eric', 'John', 'Michael'])
queue.append('Jerry')
queue.append('Graham')
print(queue)
queue.popleft()
print(queue)
queue.pop()
print(queue)
