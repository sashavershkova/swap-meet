from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, id=None, condition=0, age=None, type="Unknown"):
        super().__init__(id, condition, age)
        self.type = type

    def get_category(self):
        return "Electronics"
    
    def __str__(self):
        return super().__str__() + f" This is a {self.type} device."
