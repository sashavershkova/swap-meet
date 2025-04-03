import pytest
from swap_meet.item import Item
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_get_items_by_category():
    item_a = Clothing()
    item_b = Electronics()
    item_c = Clothing()
    item_d = Decor()
    item_e = Item()
    vendor = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )

    items = vendor.get_by_category("Clothing")

    assert len(items) == 2
    assert item_a in items
    assert item_c in items

def test_get_no_matching_items_by_category():
    item_a = Clothing()
    item_b = Item()
    item_c = Decor()
    vendor = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    items = vendor.get_by_category("Electronics")

    assert items == []

def test_best_by_category():
    item_a = Clothing(condition=2.0)
    item_b = Decor(condition=2.0)
    item_c = Clothing(condition=4.0)
    item_d = Decor(condition=5.0)
    item_e = Clothing(condition=3.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )

    best_item = tai.get_best_by_category("Clothing")

    assert best_item.get_category() == "Clothing"
    assert best_item.condition == pytest.approx(4.0)

def test_best_by_category_no_matches_is_none():
    item_a = Decor(condition=2.0)
    item_b = Decor(condition=2.0)
    item_c = Decor(condition=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    best_item = tai.get_best_by_category("Electronics")

    assert best_item is None

def test_best_by_category_with_duplicates():
    # Arrange
    item_a = Clothing(condition=2.0)
    item_b = Clothing(condition=4.0)
    item_c = Clothing(condition=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    best_item = tai.get_best_by_category("Clothing")

    assert best_item.get_category() == "Clothing"
    assert best_item.condition == pytest.approx(4.0)

def test_swap_best_by_category():
    item_a = Decor(condition=2.0)
    item_b = Electronics(condition=4.0)
    item_c = Decor(condition=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(condition=2.0)
    item_e = Decor(condition=4.0)
    item_f = Clothing(condition=4.0)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    result = tai.swap_best_by_category(
        other_vendor=jesse,
        my_priority="Clothing",
        their_priority="Decor"
    )

    assert item_f in tai.inventory
    assert item_c in jesse.inventory
    assert item_c not in tai.inventory
    assert item_f not in jesse.inventory
    assert result == True

def test_swap_best_by_category_reordered():
    # Arrange
    item_a = Decor(condition=2.0)
    item_b = Electronics(condition=4.0)
    item_c = Decor(condition=4.0)
    tai = Vendor(
        inventory=[item_c, item_b, item_a]
    )

    item_d = Clothing(condition=2.0)
    item_e = Decor(condition=4.0)
    item_f = Clothing(condition=4.0)
    jesse = Vendor(
        inventory=[item_f, item_e, item_d]
    )

    result = tai.swap_best_by_category(
        other_vendor=jesse,
        my_priority="Clothing",
        their_priority="Decor"
    )

    assert item_f in tai.inventory
    assert item_c in jesse.inventory
    assert item_c not in tai.inventory
    assert item_f not in jesse.inventory
    assert result == True

def test_swap_best_by_category_no_inventory_is_false():
    tai = Vendor(
        inventory=[]
    )

    item_a = Clothing(condition=2.0)
    item_b = Decor(condition=4.0)
    item_c = Clothing(condition=4.0)
    jesse = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    result = tai.swap_best_by_category(
        other_vendor=jesse,
        my_priority="Clothing",
        their_priority="Decor"
    )

    assert not result
    assert len(tai.inventory) == 0
    assert len(jesse.inventory) == 3
    assert item_a in jesse.inventory
    assert item_b in jesse.inventory
    assert item_c in jesse.inventory

def test_swap_best_by_category_no_other_inventory_is_false():
    item_a = Clothing(condition=2.0)
    item_b = Decor(condition=4.0)
    item_c = Clothing(condition=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    jesse = Vendor(
        inventory=[]
    )

    result = tai.swap_best_by_category(
        other_vendor=jesse,
        my_priority="Decor",
        their_priority="Clothing"
    )

    assert not result
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 0
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory

def test_swap_best_by_category_no_match_is_false():
    item_a = Decor(condition=2.0)
    item_b = Electronics(condition=4.0)
    item_c = Decor(condition=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(condition=2.0)
    item_e = Decor(condition=4.0)
    item_f = Clothing(condition=4.0)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    result = tai.swap_best_by_category(
        other_vendor=jesse,
        my_priority="Clothing",
        their_priority="Clothing"
    )

    assert result == False
    assert tai.inventory[0].get_category() != "Clothing"
    assert tai.inventory[1].get_category() != "Clothing"
    assert tai.inventory[2].get_category() != "Clothing"

def test_swap_best_by_category_no_other_match_is_false():
    item_a = Decor(condition=2.0)
    item_b = Electronics(condition=4.0)
    item_c = Decor(condition=4.0)
    tai = Vendor(
        inventory=[item_c, item_b, item_a]
    )

    item_d = Clothing(condition=2.0)
    item_e = Decor(condition=4.0)
    item_f = Clothing(condition=4.0)
    jesse = Vendor(
        inventory=[item_f, item_e, item_d]
    )

    result = tai.swap_best_by_category(
        other_vendor=jesse,
        my_priority="Electronics",
        their_priority="Decor"
    )

    assert result == False
    assert jesse.inventory[0].get_category() != "Electronics"
    assert jesse.inventory[1].get_category() != "Electronics"
    assert jesse.inventory[2].get_category() != "Electronics"

def test_get_newest_item_nominal():
    item_a = Decor(condition=2.0, age=5)
    item_b = Electronics(condition=4.0, age =3)
    item_c = Decor(condition=4.0, age=2)
    tai = Vendor(
        inventory=[item_c, item_b, item_a]
    )

    result = tai.get_newest_item()
    
    assert result == item_c

def test_get_newest_item_empty_inventory():
    tai = Vendor(inventory=[])

    result = tai.get_newest_item()
    
    assert result == None

def test_get_newest_item_age_is_None_by_default():
    item_a = Decor(condition=2.0, age=5)
    item_b = Electronics(condition=4.0)
    item_c = Decor(condition=4.0, age=2)
    tai = Vendor(
        inventory=[item_c, item_b, item_a]
    )

    result = tai.get_newest_item()
    
    assert result == item_c

def test_get_newest_item_no_ages():
    item_a = Decor(condition=2.0)
    item_b = Electronics(condition=4.0)
    item_c = Decor(condition=4.0)
    tai = Vendor(
        inventory=[item_c, item_b, item_a]
    )

    result = tai.get_newest_item()
    
    assert result == None

def test_swap_by_newest_nominal():
    item_a = Decor(condition=2.0, age=5)
    item_b = Electronics(condition=4.0, age =3)
    item_c = Decor(condition=4.0, age=2)
    tai = Vendor(
        inventory=[item_c, item_b, item_a]
    )

    item_d = Clothing(condition=2.0, age=11)
    item_e = Decor(condition=4.0, age=1)
    item_f = Clothing(condition=4.0, age=0.5)
    jesse = Vendor(
        inventory=[item_f, item_e, item_d]
    )

    result = tai.swap_by_newest(
        other_vendor=jesse)
    
    assert result == True
    assert item_c in jesse.inventory
    assert item_f in tai.inventory

def test_swap_by_newest_same_ages_in_inventory():
    item_a = Decor(condition=2.0, age=2)
    item_b = Electronics(condition=4.0, age =3)
    item_c = Decor(condition=4.0, age=2)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(condition=2.0, age=11)
    item_e = Decor(condition=4.0, age=1)
    item_f = Clothing(condition=4.0, age=1)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    result = tai.swap_by_newest(
        other_vendor=jesse)
    
    assert result == True
    assert item_a in jesse.inventory
    assert item_e in tai.inventory

def test_swap_by_newest_empty_inventory():
    tai = Vendor(inventory=[])

    item_d = Clothing(condition=2.0, age=11)
    item_e = Decor(condition=4.0, age=1)
    item_f = Clothing(condition=4.0, age=1)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    result = tai.swap_by_newest(
        other_vendor=jesse)
    
    assert result == False

def test_swap_by_newest_empty_inventory_other():
    item_a = Decor(condition=2.0, age=2)
    item_b = Electronics(condition=4.0, age =3)
    item_c = Decor(condition=4.0, age=2)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    jesse = Vendor(inventory=[])

    result = tai.swap_by_newest(
        other_vendor=jesse)
    
    assert result == False

def test_swap_by_newest_default_ages_in_inventory():
    item_a = Decor(condition=2.0)
    item_b = Electronics(condition=4.0)
    item_c = Decor(condition=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(condition=2.0, age=11)
    item_e = Decor(condition=4.0, age=1)
    item_f = Clothing(condition=4.0, age=1)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    result = tai.swap_by_newest(
        other_vendor=jesse)
    
    assert result == False

def test_swap_by_newest_default_ages_in_inventory_other():
    item_a = Decor(condition=2.0, age=11)
    item_b = Electronics(condition=4.0, age=1)
    item_c = Decor(condition=4.0, age=1)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(condition=2.0)
    item_e = Decor(condition=4.0)
    item_f = Clothing(condition=4.0)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    result = tai.swap_by_newest(
        other_vendor=jesse)
    
    assert result == False

def test_swap_by_newest_default_ages_in_both_inventories():
    item_a = Decor(condition=2.0)
    item_b = Electronics(condition=4.0)
    item_c = Decor(condition=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(condition=2.0)
    item_e = Decor(condition=4.0)
    item_f = Clothing(condition=4.0)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    result = tai.swap_by_newest(
        other_vendor=jesse)
    
    assert result == False

def test_id_string():
    item_a = Decor(id="something", condition=2.0)
    item_b = Electronics(condition=4.0)
    item_c = Decor(condition=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    result = tai.inventory[0].id
    
    assert isinstance(result, int)

def test_condition_is_string():
    item_a = Decor(condition="something")
    tai = Vendor(inventory=[item_a])

    result = tai.inventory[0].condition
    
    assert result == 0