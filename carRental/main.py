import sqlite3
from car import Car
from place import RentalPlace


conn = sqlite3.connect("carRental.db")
c = conn.cursor()


car1 = Car("red", "Tesla", "X", "HF 33 900")
car2 = Car("blue", "Tesla", "X", "EG 87 239")
car3 = Car("green", "Tesla", "X", "JU 54 895")

# try:
place1 = RentalPlace("HU1", 3)
place1.add_car(car1)
place1.add_car(car2)
place1.add_car(car3)
# place1.rmv_car(car1)
# except Exception as e:
#    print("Error!", e)
