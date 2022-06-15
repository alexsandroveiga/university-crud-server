import math
from controllers import Controller
from infra import *
from helpers import ok

class ListOrdersController(Controller):
  def perform(self, request):
    id = request.args.get("id", default=1, type=str)
    order = Order.select().where(Order.id == id).dicts()
    for item in order:
      item['customer'] = Customer.select().where(Customer.id == item['customer']).first().__data__
      item['motorcycles'] = list(OrderMotorcycles.select().where(OrderMotorcycles.order == item['id']).dicts())
    return ok(list(order))