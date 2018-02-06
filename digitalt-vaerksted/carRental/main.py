from car import Car
from place import RentalPlace


car1 = Car("red", "Tesla", "X", "HF 33 900")
car2 = Car("blue", "Tesla", "X", "EG 87 239")
car3 = Car("green", "Tesla", "X", "JU 54 895")

try:
    place1 = RentalPlace("HU1", 2)
    place1.add_car(car1)
    place1.add_car(car2)
    place1.add_car(car3)
except Exception as e:
    print("Error!", e)

for i in place1.carsInStock:
    print(i.get_numPlate())
