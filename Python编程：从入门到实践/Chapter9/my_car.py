from car import Car

my_car = Car('tesla', 'model Y', 2020)
print(my_car.get_descriptive_name())

my_car.update_odometer(23)
my_car.read_odometer()
