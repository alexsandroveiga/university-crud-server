from infra import *
from controllers import Controller
from helpers import *

class CreateOrderController(Controller):
  def perform(self, request):
    try:
      order = Order.create(**request.json)
      for item in request.json['motorcycles']:
        moto = Motorcycle.select().where(Motorcycle.id == item['motorcycle']).first()
        if moto:
          quantity = moto.quantity - item['quantity']
          if quantity < 0:
            raise(Exception('Not enough motorcycles'))
          Motorcycle.update({ Motorcycle.quantity: quantity }).where(Motorcycle.id == item['motorcycle']).execute()
        OrderMotorcycles.create(order=order, motorcycle=item['motorcycle'], quantity=item['quantity'], price=item['price'])
      return ok(order.__data__)
    except Exception as error:
      return bad_request(str(error))