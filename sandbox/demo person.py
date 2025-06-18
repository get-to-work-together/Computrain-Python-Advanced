
class Person:

    def __init__(self, name, residence):
        # attributes
        self.name = name
        self.residence = residence

    # methods
    def tell(self):
        print(f'Ik ben {self.name} en ik woon in {self.residence}.')

    def move(self, new_residence):
        self.residence = new_residence


class Customer(Person):

    def __init__(self, name, residence, customernr):
        # attributes
        super().__init__(name, residence)
        self.customernr = customernr

    def tell(self):
        print(f'Ik ben {self.name} uit {self.residence} en een VIP klant ({self.customernr}).')


# -----------------------------------------------------

p1 = Person('Peter', 'Lhee')   # instantiation
p2 = Customer('Paul', 'Linschoten', 'NL7653998')

p1.tell()
p2.tell()

p1.move('Utrecht')

p1.tell()
p2.tell()
