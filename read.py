from flask import Flask
from flask_login import LoginManager
from lib.dao.inventory_dao import Warehouse
from lib.dao.user_dao import UserManager
from lib.shopping_data import OnlineShoppingData

# Loads data
warehouse = Warehouse.load_data()
user_db = UserManager.load_data()
user_db.read()








