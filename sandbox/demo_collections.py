from collections import deque

l = [1,2,3,4]
l.append(5)
l.append(6)
l.pop(0)

print(l)

d = deque([1,2,3,4])
d.append(5)
d.append(6)
d.popleft()

print(d)