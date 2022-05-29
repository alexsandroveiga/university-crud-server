from flask import Flask

from controllers import *
from main.adapters import *

def route(app: Flask):
  @app.route('/motorcycles', methods=['POST'])
  def motorcycle_create():
    return adapt_flask_route(CreateMotorcycleController())

  @app.route('/motorcycles', methods=['GET'])
  def motorcycle_read():
    return adapt_flask_route(ListMotorcyclesController())

  @app.route('/motorcycles/<id>', methods=['DELETE'])
  def motorcycle_delete(id):
    return adapt_flask_route(DeleteMotorcycleController())
    