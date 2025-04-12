from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, id=None, condition=0, age=None, fabric="Unknown"):
        super().__init__(id, condition, age)
        self.fabric = fabric

    def get_category(self):
        return "Clothing"
    
    def __str__(self):
        return super().__str__() + f" It is made from {self.fabric} fabric."