from flask import Flask
from flask_login import LoginManager
from lib.dao.inventory_dao import Warehouse
from lib.dao.user_dao import UserManager
from lib.shopping_data import OnlineShoppingData


app = Flask(__name__)
app.secret_key = 'very-secret-123'  # Used to add entropy
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


# Loads data
warehouse = Warehouse.load_data()
user_db = UserManager.load_data()
# warehouse, user_db = OnlineShoppingData.load_data()
