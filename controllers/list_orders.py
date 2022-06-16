import math
from controllers import Controller
from infra import *
from helpers import *

class ListOrdersController(Controller):
  def perform(self, request):
    order = Order.select().join(Customer).dicts().order_by(Order.id.desc())
    for item in order:
      item['customer'] = Customer.select().where(Customer.id == item['customer']).first().__data__
      item['motorcycles'] = list(OrderMotorcycles.select().where(OrderMotorcycles.order == item['id']).dicts())
    return ok(list(order))