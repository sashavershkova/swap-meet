class Vendor:
    def __init__(self, inventory=None):
        if inventory is None or not isinstance(inventory, list):
            inventory = []
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item
        
    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
                return False
        
        self.remove(my_item)
        other_vendor.add(my_item)
        other_vendor.remove(their_item)
        self.add(their_item)
        return True

    
    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
              
        return self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])
    
    def get_by_category(self, category):
        return [item for item in self.inventory if item.get_category() == category]
    
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

        return self.swap_items(other_vendor, item_other_vendor_wants, item_self_wants)
    
    def get_newest_item(self):
        if not self.inventory:
            return None
        
        newest_item = None

        for item in self.inventory:
            # skip this item if it has no age (guard clause)
            if item.age is None:
                continue

            # we found an item with age
            # update if this is the first found, or if better than the previous
            if newest_item is None or item.age < newest_item.age:
                newest_item = item
        
        return newest_item


    def swap_by_newest(self, other_vendor):
        self_newest_item = self.get_newest_item()
        other_vendor_newest_item = other_vendor.get_newest_item()

        if not self_newest_item or not other_vendor_newest_item:
            return False
        
        self.swap_items(other_vendor, self_newest_item, other_vendor_newest_item)
        return True





