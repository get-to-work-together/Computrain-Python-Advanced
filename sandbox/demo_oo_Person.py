class Person:

    __slots__ = ['_name', '_residence']

    def __init__(self, name, residence):
        self._name = name
        self._residence = residence

    def tell(self):
        return f'Ik ben {self._name} en ik woon in {self._residence}.'

    def move(self, new_residence):
        self._residence = new_residence


class Customer(Person):

    def __init__(self, name, residence, klantnr):
        super().__init__(name, residence)
        self._klantnr = klantnr

    def tell(self):
        return f'Ik ben klant {self._name} en met klantnummer {self._klantnr}.'

# --------------------------------

p = Person('Albert', 'Amsterdam')

print( p.tell() )
p.move('Utrecht')
print( p.tell() )

c = Customer('Jan', 'Amsterdam', 43567)
print( c.tell() )