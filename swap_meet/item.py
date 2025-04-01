
import uuid

class Item:
    def __init__(self, id=None, condition=0):
        if id is not None:
            self.id = id
        else:
            self.id = uuid.uuid4().int  # long unique number
        self.condition = condition

    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."

