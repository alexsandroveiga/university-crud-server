import math
from controllers import Controller
from infra import *
from helpers import *

class ListOrdersController(Controller):
  def perform(self, request):
    order = Order.select().join(Customer).dicts().order_by(Order.id.desc())
    for item in order:
      item['customer'] = Customer.select().where(Customer.id == item['customer']).first().__data__
      order_motorcycle = OrderMotorcycles.select().where(OrderMotorcycles.order == item['id']).dicts()
      for item_motorcycle in order_motorcycle:
        item_motorcycle['motorcycle'] = Motorcycle.select().where(Motorcycle.id == item_motorcycle['motorcycle']).first().__data__
      item['motorcycles'] = list(order_motorcycle)
    return ok(list(order))