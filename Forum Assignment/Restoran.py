class RestoJo:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        
    def __PriceList(self):
        if self.name == "Dry Cured Iberian Ham":
            y = 177.80
        elif self.name == "Wagyu Steak":
            y = 450.00
        elif self.name == "Matsutake Mushrooms":
            y = 272.00
        elif self.name == "Kopi Luwak Coffee":
            y = 306.50
        elif self.name == "Moose Cheese":
            y = 487.20
        elif self.name == "White Truffles":
            y = 3600.00
        elif self.name == "Blue Fin Tuna":
            y = 3603.00
        elif self.name == "Le Bonnotte Potatoes":
            y = 270.81
        else:
            y = 0.00
        return y

    def CalcPrice(self):
        x = self.weight * self.__PriceList()
        return x
