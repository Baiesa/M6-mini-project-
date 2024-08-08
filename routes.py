from flask import Blueprint, request, jsonify
from models import Customer, CustomerAccount, Product, Order
from app import db

customer_routes = Blueprint('customer_routes', __name__, url_prefix='/customers')
customer_account_routes = Blueprint('customer_account_routes', __name__, url_prefix='/customeraccounts')
product_routes = Blueprint('product_routes', __name__, url_prefix='/products')
order_routes = Blueprint('order_routes', __name__, url_prefix='/orders')

# Customer Routes
@customer_routes.route('', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    return jsonify([c.to_dict() for c in customers])

@customer_routes.route('', methods=['POST'])
def create_customer():
    data = request.json
    customer = Customer(**data)
    db.session.add(customer)
    db.session.commit()
    return jsonify(customer.to_dict()), 201

@customer_routes.route('/<int:id>', methods=['GET'])
def get_customer(id):
    customer = Customer.query.get_or_404(id)
    return jsonify(customer.to_dict())

@customer_routes.route('/<int:id>', methods=['PUT'])
def update_customer(id):
    data = request.json
    customer = Customer.query.get_or_404(id)
    for key, value in data.items():
        setattr(customer, key, value)
    db.session.commit()
    return jsonify(customer.to_dict())

@customer_routes.route('/<int:id>', methods=['DELETE'])
def delete_customer(id):
    customer = Customer.query.get_or_404(id)
    db.session.delete(customer)
    db.session.commit()
    return '', 204

# CustomerAccount Routes
@customer_account_routes.route('', methods=['GET'])
def get_customer_accounts():
    accounts = CustomerAccount.query.all()
    return jsonify([a.to_dict() for a in accounts])

@customer_account_routes.route('', methods=['POST'])
def create_customer_account():
    data = request.json
    account = CustomerAccount(**data)
    db.session.add(account)
    db.session.commit()
    return jsonify(account.to_dict()), 201

@customer_account_routes.route('/<int:id>', methods=['GET'])
def get_customer_account(id):
    account = CustomerAccount.query.get_or_404(id)
    return jsonify(account.to_dict())

@customer_account_routes.route('/<int:id>', methods=['PUT'])
def update_customer_account(id):
    data = request.json
    account = CustomerAccount.query.get_or_404(id)
    for key, value in data.items():
        setattr(account, key, value)
    db.session.commit()
    return jsonify(account.to_dict())

@customer_account_routes.route('/<int:id>', methods=['DELETE'])
def delete_customer_account(id):
    account = CustomerAccount.query.get_or_404(id)
    db.session.delete(account)
    db.session.commit()
    return '', 204

# Product Routes
@product_routes.route('', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([p.to_dict() for p in products])

@product_routes.route('', methods=['POST'])
def create_product():
    data = request.json
    product = Product(**data)
    db.session.add(product)
    db.session.commit()
    return jsonify(product.to_dict()), 201

@product_routes.route('/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get_or_404(id)
    return jsonify(product.to_dict())

@product_routes.route('/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.json
    product = Product.query.get_or_404(id)
    for key, value in data.items():
        setattr(product, key, value)
    db.session.commit()
    return jsonify(product.to_dict())

@product_routes.route('/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return '', 204

# Order Routes
@order_routes.route('', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return jsonify([o.to_dict() for o in orders])

@order_routes.route('', methods=['POST'])
def create_order():
    data = request.json
    order = Order(**data)
    db.session.add(order)
    db.session.commit()
    return jsonify(order.to_dict()), 201

@order_routes.route('/<int:id>', methods=['GET'])
def get_order(id):
    order = Order.query.get_or_404(id)
    return jsonify(order.to_dict())

@order_routes.route('/<int:id>', methods=['PUT'])
def update_order(id):
    data = request.json
    order = Order.query.get_or_404(id)
    for key, value in data.items():
        setattr(order, key, value)
    db.session.commit()
    return jsonify(order.to_dict())

@order_routes.route('/<int:id>', methods=['DELETE'])
def delete_order(id):
    order = Order.query.get_or_404(id)
    db.session.delete(order)
    db.session.commit()
    return '', 204