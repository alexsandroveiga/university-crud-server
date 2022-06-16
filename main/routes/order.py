from flask import Flask

from controllers import *
from main.adapters import *

def route(app: Flask):
  @app.route('/orders', methods=['POST'])
  def order_create():
    return adapt_flask_route(CreateOrderController())
  
  @app.route('/orders', methods=['GET'])
  def order_read():
    return adapt_flask_route(ListOrdersController())

  @app.route('/orders/<id>', methods=['DELETE'])
  def order_delete(id):
    return adapt_flask_route(DeleteOrderController())