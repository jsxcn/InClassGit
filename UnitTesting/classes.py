class Car:
    def __init__(self, name, year)
        self.name = name
        self.year = year

car1 = Car("Tesla Model 3", 2017)
car2 = Car("Honda", 1980)
# print(car1)
# print(car2)
# print(car1.name)
# print(car2.name)


#inheritance
class electricCars(Car):
    pass 

ec1=electricCars("Roadster", 2020)
print(ec1.name) # name and year are inherited from parents 