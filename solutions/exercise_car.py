class Car:
    """This is my own Car class"""

    def __init__(self, make, type, color, mileage = 0):
        """Dit is de __init__ method with 4 arguments"""
        self._make = make
        self._type = type
        self._color = color
        self._mileage = mileage

    def __str__(self):
        """return a string with information about the car"""
        return f"My car is a {self._color} {self._make} {self._type}. " \
               f"Mileage: {self._mileage}."

    def __repr__(self):
        return f"Car('{self._make}', '{self._type}', '{self._color}')"

    def info(self):
        """return a string with information about the car"""
        return f"My car is a {self._color} {self._make} {self._type}. " \
               f"Mileage: {self._mileage}."

    def drive(self, distance):
        """drive a distance and increment the mileage"""
        self._mileage += distance
        print( f'Driving {distance} km.')


# -----------------------------------

car = Car('Volkswagen', 'Kever', 'Red')

print( car.info() )

car.drive(123)
car.drive(12)
car.drive(104)

print( car.info() )
