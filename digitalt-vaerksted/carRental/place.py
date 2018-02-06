class RentalPlace(object):
    def __init__(self, name, cap):
        self.carsInStock = []
        self.name = name
        self.cap = cap

    def get_name(self):
        return self.name

    def set_name(self, newName):
        self.name = newName

    def get_cap(self):
        return self.cap

    def set_cap(self, newCap):
        self.cap = newCap

    def get_carsInStock(self):
        return self.carsInStock

    def add_car(self, car):
        try:
            if len(self.carsInStock) < self.cap:
                self.carsInStock.append(car)
            else:
                raise Exception("Rental place is full")
        except Exception as assExp:
            raise

    def rmv_car(self, car):
        for i in list(self.carsInStock):
            if i.get_numPlate() == car.get_numPlate():
                self.carsInStock.remove(i)
