from flask import Flask

from controllers import *
from main.adapters import *

def route(app: Flask):
  @app.route('/customers', methods=['POST'])
  def customer_create():
    return adapt_flask_route(CreateCustomerController())

  @app.route('/customers', methods=['GET'])
  def customer_read():
    return adapt_flask_route(ListCustomersController())
    