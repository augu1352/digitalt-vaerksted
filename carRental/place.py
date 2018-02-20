import sqlite3
conn = sqlite3.connect("carRental.db")
c = conn.cursor()


class RentalPlace(object):
    def __init__(self, name, cap):
        self.carsInStock = []
        self.name = name
        self.cap = cap
        self.placeId = 0
        c.execute("INSERT INTO PLACE(name, cap) VALUES(?, ?)", (self.name, self.cap))

    def get_name(self):
        return self.name

    def set_name(self, newName):
        self.name = newName

    def get_cap(self):
        return self.cap

    def set_cap(self, newCap):
        self.cap = newCap

    def get_placeId(self):
        return self.placeId

    def set_placeId(self, newPlaceId):
        placeId = newPlaceId

    def get_carsInStock(self):
        return self.carsInStock

    def add_car(self, car):
        try:
            if len(self.carsInStock) < self.cap:
                self.carsInStock.append(car)
                c.execute("INSERT INTO CAR(color, brand, model, numPlate) VALUES(?, ?, ?, ?)", (car.color, car.brand, car.model, car.numPlate))
                conn.commit()
            else:
                raise Exception("Rental place is full")
        except Exception as assExp:
            raise

    def rmv_car(self, car):
        for i in list(self.carsInStock):
            if i.get_carId() == car.get_carId():
                self.carsInStock.remove(i)
                c.execute("DELETE FROM CAR WHERE carId = ?", (car.get_carId(),))
                conn.commit()
