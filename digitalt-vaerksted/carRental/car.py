class Car(object):
    def __init__(self, color, brand, model, numPlate):
        self.color = color
        self.brand = brand
        self.model = model
        self.numPlate = numPlate

    def get_color(self):
        return self.color

    def set_color(self, newColor):
        self.color = newColor

    def get_brand(self):
        return self.brand

    def set_brand(self, newBrand):
        self.brand = newBrand

    def get_model(self):
        return self.model

    def set_model(self, newModel):
        self.model = newModel

    def get_numPlate(self):
        return self.numPlate

    def set_numPlate(self, newNumPlate):
        self.numPlate = newNumPlate
