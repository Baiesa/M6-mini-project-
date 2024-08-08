from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import Config

# Create a single instance of SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    

    db.init_app(app)
    
   
    CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

    with app.app_context():
        from routes import customer_routes, customer_account_routes, product_routes, order_routes
        app.register_blueprint(customer_routes)
        app.register_blueprint(customer_account_routes)
        app.register_blueprint(product_routes)
        app.register_blueprint(order_routes)

    @app.route('/')
    def index():
        return "Welcome to the API. Use the appropriate endpoints to access resources."

    @app.after_request
    def add_cors_headers(response):
        response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
        return response

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)