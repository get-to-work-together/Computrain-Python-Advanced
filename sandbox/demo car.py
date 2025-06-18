class Car:

    def __init__(self, make, model, color, mileage = 0):
        self.make = make
        self.model = model
        self.color = color
        self.mileage = mileage

    def info(self):
        print(f'This beautiful {self.color} {self.make} {self.model} has a mileage of {self.mileage} km.')

    def drive(self, distance):
        self.mileage += distance


# --------------------------------------------------------

my_car = Car('Renault', 'Megane station', 'metalic brown', 497200)

my_car.info()
my_car.drive(166)
my_car.drive(166)
my_car.info()
