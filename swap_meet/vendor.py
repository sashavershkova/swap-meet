class Vendor:
    def __init__(self, inventory = None):
        if not inventory:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else: 
            return False
        
    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item in self.inventory and their_item in other_vendor.inventory:
            self.remove(my_item)
            other_vendor.add(my_item)
            other_vendor.remove(their_item)
            self.add(their_item)
            return True
        return False
    
    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        
        self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])
        return True
    
    def get_by_category(self, category):
        inventory_by_cat = []
        for item in self.inventory:
            if item.get_category() == category:
                inventory_by_cat.append(item)
        return inventory_by_cat
    
    def get_best_by_category(self, category):
        inventory_by_cat = self.get_by_category(category)
        best_condition = 0
        best_item = None
        for item in inventory_by_cat:
            if item.condition > best_condition:
                best_condition = item.condition
                best_item = item
        return best_item

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        item_self_wants = other_vendor.get_best_by_category(my_priority)
        item_other_vendor_wants = self.get_best_by_category(their_priority)
        if item_self_wants is None or item_other_vendor_wants is None:
            return False
        self.swap_items(other_vendor, item_other_vendor_wants, item_self_wants)
        return True


