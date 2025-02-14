from flask import Flask
from .views import customer_bp
import os

# class Config:
#     SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key_here'
#     MYSQL_PORT = 3306
#     MYSQL_HOST = 'localhost'
#     MYSQL_USER = 'root'
#     MYSQL_PASSWORD = 'root'
#     MYSQL_DB = 'Movie_Booking'

# def create_app():
#     app = Flask(__name__)
#     app.config.from_object(Config())

#     # Register Blueprints
#     app.register_blueprint(customer_bp)

#     return app