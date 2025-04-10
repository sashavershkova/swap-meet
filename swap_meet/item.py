
import uuid

class Item:
    def __init__(self, id=None, condition=0, age=None):
        if id is not None and isinstance(id, int):
            self.id = id
        else:
            self.id = uuid.uuid4().int  # long unique number

        if isinstance(condition, (int, float)) and 1.0 <= condition <= 5.0:
            self.condition = condition
        else:
            self.condition = 0
            
        self.age = age

    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."
    
    def condition_description(self):
        if self.condition == 0:
            return "Unusable"
        elif self.condition == 1:
            return "Poor"
        elif self.condition == 2:
            return "Fair"
        elif self.condition == 3:
            return "Good"
        elif self.condition == 4:
            return "Very good"
        elif self.condition == 5:
            return "Like new"
        

