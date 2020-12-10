import pytest
from lib.dao.inventory_dao import Warehouse
from lib.products import *

@pytest.fixture
def warehouse_fixture():
    warehouse = Warehouse()
    warehouse.add_item(Shirt("Cool Shirt", 25.2, 'S', 'Red'))
    warehouse.add_item(Shirt("Oversized Shirt", 50.59, 'XL', 'Green'))
    warehouse.add_item(Shirt("Gucci Mane", 713.1, 'M', 'Brown/Orange'))
    warehouse.add_item(Shirt("Basics Range", 9.95, 'S', 'White'))
    warehouse.add_item(Shirt("Google Attire", 25.2, 'S', 'Multi'))

    warehouse.add_item(Pants("Basics Range", 19.95, 'S', 'White'))
    warehouse.add_item(Pants("Jeans", 70.0, 'M', 'Jeans'))

    warehouse.add_item(Accessories("Blue Cool Earrings", 70.35, 'OneSize', 'Blue'))
    warehouse.add_item(Accessories("Schooler Hat", 19.95, 'M', 'Yellow'))

    return warehouse


#### User Story 1 - General search ####
def test_general_search(warehouse_fixture):
    text = "Cool"
    result = warehouse_fixture.search_all(text)

    for i in result:
        assert(text in i.name)

def test_general_search_insensitive(warehouse_fixture):
    text = "cOOl"
    result = warehouse_fixture.search_all(text)
    lower_text = text.lower()
    for i in result:
        assert(lower_text in i.name.lower())

def test_general_search_no_match(warehouse_fixture):
    text = "NOT FOUND 123"

    result = warehouse_fixture.search_all(text)

    assert(len(result) == 0)

def test_general_search_exact_name(warehouse_fixture):
    text = "Schooler Hat"

    result = warehouse_fixture.search_all(text)
    assert(len(result) == 1)
    for i in result:
        assert(i.name == text)


#### User Story 2 - Category ####
def test_cat_search(warehouse_fixture):
    text = "Cool"
    result = warehouse_fixture.search_cat(Clothing.__name__, text)

    for i in result:
        assert(text in i.name)

def test_cat_search_insensitive(warehouse_fixture):
    text = "cOOl"
    result = warehouse_fixture.search_cat(Clothing.__name__, text)

    lower_text = text.lower()
    for i in result:
        assert(lower_text in i.name.lower())

def test_cat_search_no_match(warehouse_fixture):
    text = "NOT FOUND 123"

    result = warehouse_fixture.search_cat(Clothing.__name__, text)

    assert(len(result) == 0)

def test_cat_search_exact_name(warehouse_fixture):
    text = "Gucci Mane"
    result = warehouse_fixture.search_cat(Clothing.__name__, text)
    assert(len(result) == 1)
    for i in result:
        assert(i.name == text)


#### User Story 2 - Subcategory ####
def test_subcat_search(warehouse_fixture):
    text = "Cool"
    result = warehouse_fixture.search_subcat(Shirt.__name__, text)

    for i in result:
        assert(text in i.name)

def test_subcat_search_insensitive(warehouse_fixture):
    text = "cOOl"
    result = warehouse_fixture.search_subcat(Shirt.__name__, text)

    lower_text = text.lower()
    for i in result:
        assert(lower_text in i.name.lower())

def test_subcat_search_no_match(warehouse_fixture):
    text = "NOT FOUND 123"

    result = warehouse_fixture.search_subcat(Shirt.__name__, text)

    assert(len(result) == 0)

def test_subcat_search_exact_name(warehouse_fixture):
    text = "Gucci Mane"
    result = warehouse_fixture.search_subcat(Shirt.__name__, text)
    assert(len(result) == 1)
    for i in result:
        assert(i.name == text)
