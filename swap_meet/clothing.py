from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, id=None, fabric="Unknown", condition=0):
        super().__init__(id, condition)
        self.fabric = fabric
    
    def __str__(self):
        return super().__str__() + f" It is made from {self.fabric} fabric."