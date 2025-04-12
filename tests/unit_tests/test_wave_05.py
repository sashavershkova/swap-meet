import pytest
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics
from swap_meet.item import Item

TEST_CUSTOM_ID = 12345

# ~~~~~ Clothing Tests ~~~~~

def test_clothing_has_default_uuid_length_id():
    clothing = Clothing()
    check_for_default_uuid_length_id(clothing)

def test_clothing_has_expected_category_and_custom_id():
    clothing = Clothing(id=TEST_CUSTOM_ID)
    check_category_and_custom_id(clothing, TEST_CUSTOM_ID, "Clothing")

def test_clothing_has_expected_default_to_str():
    clothing = Clothing(id=TEST_CUSTOM_ID)
    expected_str = (
        f"An object of type Clothing with id {TEST_CUSTOM_ID}. "
        "It is made from Unknown fabric."
    )
    assert str(clothing) == expected_str

def test_clothing_has_expected_to_str_with_custom_fabric():
    clothing = Clothing(id=TEST_CUSTOM_ID, fabric="Pinstriped")
    expected_str = (
        f"An object of type Clothing with id {TEST_CUSTOM_ID}. "
        "It is made from Pinstriped fabric."
    )
    assert str(clothing) == expected_str

# ~~~~~ Decor Tests ~~~~~

def test_decor_has_default_uuid_length_id():
    decor = Decor()
    check_for_default_uuid_length_id(decor)

def test_decor_has_expected_category_and_custom_id():
    decor = Decor(id=TEST_CUSTOM_ID)
    check_category_and_custom_id(decor, TEST_CUSTOM_ID, "Decor")

def test_decor_has_expected_default_to_str():
    decor = Decor(id=TEST_CUSTOM_ID)
    expected_str = (
        f"An object of type Decor with id {TEST_CUSTOM_ID}. "
        "It takes up a 0 by 0 sized space."
    )
    assert str(decor) == expected_str

def test_decor_has_expected_to_str_with_custom_size():
    decor = Decor(id=TEST_CUSTOM_ID, width=3, length=12)
    expected_str = (
        f"An object of type Decor with id {TEST_CUSTOM_ID}. "
        "It takes up a 3 by 12 sized space."
    )
    assert str(decor) == expected_str

# ~~~~~ Electronics Tests ~~~~~

def test_electronics_has_default_uuid_length_id():
    electronics = Electronics()
    check_for_default_uuid_length_id(electronics)

def test_electronics_has_expected_category_and_custom_id():
    electronics = Electronics(id=TEST_CUSTOM_ID)
    check_category_and_custom_id(electronics, TEST_CUSTOM_ID, "Electronics")

def test_electronics_has_expected_default_to_str():
    electronics = Electronics(id=TEST_CUSTOM_ID)
    expected_str = (
        f"An object of type Electronics with id {TEST_CUSTOM_ID}. "
        "This is a Unknown device."
    )
    assert str(electronics) == expected_str

def test_electronics_has_expected_to_str_with_custom_type():
    electronics = Electronics(id=TEST_CUSTOM_ID, type="Mobile Phone")
    expected_str = (
        f"An object of type Electronics with id {TEST_CUSTOM_ID}. "
        "This is a Mobile Phone device."
    )
    assert str(electronics) == expected_str


# ~~~~~ Item Tests ~~~~~

def test_items_have_condition_as_float():
    items = [
        Clothing(condition=3.5),
        Decor(condition=3.5),
        Electronics(condition=3.5)
    ]
    for item in items:
        assert item.condition == pytest.approx(3.5)

def test_items_have_condition_as_float_and_gets_appropriate_description():
    unusable_item1 = Item(condition=0.0)
    unusable_item2 = Item(condition=0.22)
    unusable_item3 = Item(condition=0.49)
    poor_item1 = Item(condition=0.50)
    poor_item2 = Item(condition=0.7)
    poor_item3 = Item(condition=1.49)
    fair_item1 = Item(condition=1.50)
    fair_item2 = Item(condition=2.1)
    fair_item3 = Item(condition=2.49)
    good_item1 = Item(condition=2.50)
    good_item2 = Item(condition=3.1)
    good_item3 = Item(condition=3.49)
    very_good_item1 = Item(condition=3.50)
    very_good_item2 = Item(condition=4.2)
    very_good_item3 = Item(condition=4.49)
    like_new_item1 = Item(condition=4.50)
    like_new_item2 = Item(condition=4.7)
    like_new_item3 = Item(condition=5.0)

    assert unusable_item1.condition_description() == "Unusable"
    assert unusable_item2.condition_description() == "Unusable"
    assert unusable_item3.condition_description() == "Unusable"
    assert poor_item1.condition_description() == "Poor"
    assert poor_item2.condition_description() == "Poor"
    assert poor_item3.condition_description() == "Poor"   
    assert fair_item1.condition_description() == "Fair"
    assert fair_item2.condition_description() == "Fair"
    assert fair_item3.condition_description() == "Fair"
    assert good_item1.condition_description() == "Good"
    assert good_item2.condition_description() == "Good"
    assert good_item3.condition_description() == "Good"
    assert very_good_item1.condition_description() == "Very good"
    assert very_good_item2.condition_description() == "Very good"
    assert very_good_item3.condition_description() == "Very good"
    assert like_new_item1.condition_description() == "Like new"

def test_items_have_condition_descriptions_that_are_the_same_regardless_of_type():
    items = [
        Clothing(condition=5),
        Decor(condition=5),
        Electronics(condition=5)
    ]
    five_condition_description = items[0].condition_description()
    assert isinstance(five_condition_description, str)
    for item in items:
        assert item.condition_description() == five_condition_description
    items[0].condition = 1
    one_condition_description = items[0].condition_description()
    assert isinstance(one_condition_description, str)
    for item in items:
        item.condition = 1
        assert item.condition_description() == one_condition_description

    assert one_condition_description != five_condition_description

# ~~~~~ Helper Functions ~~~~~

def check_for_default_uuid_length_id(to_check):
    assert isinstance(to_check.id, int)
    assert len(str(to_check.id)) >= 32

def check_category_and_custom_id(to_check, id, category):
    assert to_check.get_category() == category
    assert to_check.id == id