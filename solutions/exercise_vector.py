
class Vector:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __repr__(self):
        return f'Vector({self._x}, {self._y})'

    def __str__(self):
        return f'[{self._x}, {self._y}]'

    def __add__(self, other):
        return Vector(self._x + other._x, self._y + other._y)

    def __gt__(self, other):
        return self.length() > other.length()

    def __lt__(self, other):
        return self.length() < other.length()

    def length(self):
        return (self._x ** 2 + self._y ** 2) ** 0.5

# ---------------------------------------------------------


v1 = Vector(3, 2)
v2 = Vector(1, 1)

v3 = v1 + v2

print(repr(v1))
print(repr(v2))
print(repr(v3))

print(f'{v1} + {v2} = {v3}')

if v1 > v2:
    print('v1 is longer then v2')
elif v1 < v2:
    print('v2 is longer then v1')
else:
    print('v2 and v1 are equally long')