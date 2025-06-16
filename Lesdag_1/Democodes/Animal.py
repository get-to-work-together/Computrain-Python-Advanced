class Animal():

    def __init__(self, name):
        self._name = name

    def tell(self):
        return self._name + " gives sound."


class Fish(Animal):

    def __init__(self, name):
        super().__init__(name)

    def tell(self):
        return self._name + " gives blub."

class Dog(Animal):

    def __init__(self, name):
        super().__init__(name)

    def tell(self):
        return self._name + " barks."



animalRicky = Dog("Ricky")
animalAmber = Fish("Amber")
generalAnimal = Animal("Martijn")

print(animalRicky.tell())
print(animalAmber.tell())
print(generalAnimal.tell())


