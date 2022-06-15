from infra import *
from controllers import Controller
from helpers import *

class CreateOrderController(Controller):
  def perform(self, request):
    order = Order.create(**request.json)
    for item in request.json['motorcycles']:
      OrderMotorcycles.create(order=order, motorcycle=item['motorcycle'], quantity=item['quantity'], price=item['price'])
    return ok(order.__data__)