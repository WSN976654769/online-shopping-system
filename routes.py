from functools import wraps
from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_required, login_user, logout_user
from server import app, login_manager, warehouse, user_db
from lib.products import ALL_ITEMS, CATEGORIES, CLOTHING, CAMPING


@login_manager.user_loader
def load_user(user_id):
    return user_db.find_by_id(user_id)


def admin_required(f):
    """This is used to check the admin status of the user"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.admin:
            return redirect(url_for('page_not_found'))
        return f(*args, **kwargs)
    return decorated_function


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/add_product')
@login_required
@admin_required
def add_product():
    return render_template('add_product.html', choices=ALL_ITEMS.keys())


@app.route('/create_product', methods=['GET', 'POST'])
@login_required
@admin_required
def create_product():
    if request.method == 'POST':
        # User wants to create the product
        category = request.form['category']

        args = request.form.to_dict()
        del args['category']  # We don't need to keep track of the category to build it
        builder = ALL_ITEMS[category]
        item = builder(**args)
        warehouse.add_item(item)
    else:
        # Choose a category
        category = request.args.get('category', 'Accessories')

    return render_template('create_product.html', category=category, clothing=CLOTHING, camping=CAMPING)


@app.route('/search', methods=['GET', 'POST'])
@login_required
def search():
    results = []
    if request.method == 'POST':
        # Purchase from the search screen
        id = int(request.form['id'])
        qty = int(request.form['qty'])
        current_user.cart.add_to_cart(id, qty)

    if request.args.get('s') is not None:
        search_string = request.args['s']
        # Search
        select = request.args.get('select', 'all_btn')
        if select == 'cat_btn':
            results = warehouse.search_cat(request.args.get('cat', ''), search_string)
        elif select == 'sub_btn':
            results = warehouse.search_subcat(request.args.get('sub', ''), search_string)
        else:
            results = warehouse.search_all(search_string)

    return render_template('search.html', results=results,
                           hidden_traits=['_item_code'],
                           choices=[''] + list(CATEGORIES.keys()),
                           sub_choices=[''] + list(ALL_ITEMS.keys()))


@app.route('/shop', methods=['GET', 'POST'])
@login_required
def shop():
    if request.method == 'POST':
        # Add to cart
        id = int(request.form['id'])
        qty = int(request.form['qty'])
        current_user.cart.add_to_cart(id, qty)
    return render_template('shop.html', items=warehouse.get_all_items(), hidden_traits=['_item_code'])


@app.route('/checkout', methods=['GET', 'POST'])
@login_required
def checkout():
    if request.method == 'POST':
        if request.form['action'] == 'purchase':
            # Purchase entire cart
            current_user.cart.purchase_cart()
        elif request.form['action'] == 'update':
            # Update item qty
            current_user.cart.update(int(request.form['id']), int(request.form['qty']))
        elif request.form['action'] == 'remove':
            # Remove the item from the cart
            current_user.cart.remove(int(request.form['id']))

    return render_template('checkout.html',
                           table=current_user.cart.checkout(warehouse))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Checks the user before logging in
        user = user_db.validate_login(request.form['username'], request.form['password'])
        if user is None:
            return render_template('login.html')
        login_user(user)
        # Next helps with redirecting the user to their previous page
        next = request.args.get('next')
        return redirect(next or url_for('home'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/404')
@app.errorhandler(404)
def page_not_found(e=None):
    return render_template('404.html'), 404