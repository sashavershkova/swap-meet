from .constants import CONDITION_STATES
import uuid
import math

class Item:
    def __init__(self, id=None, condition=0, age=None):
        if id is not None and not isinstance(id, int):
            raise TypeError("ID has to be an integer or not provided, so it can be safely set!")
        self.id = id if id is not None else uuid.uuid4().int # long unique number  

        if not isinstance(condition, (int, float)):
            raise TypeError("Condition has to be a number between 0.0 and 5.0")
        if not (0.0 <= condition <= 5.0):
            raise ValueError("Condition has to be a number between 0.0 and 5.0")
        self.condition = condition
            
        self.age = age

    def get_category(self):
        return "Item"
    
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."
    
    def condition_description(self):
        return CONDITION_STATES[math.floor(self.condition + 0.5)]
        

