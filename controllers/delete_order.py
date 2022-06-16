from infra import *
from helpers import *
from controllers import Controller

class DeleteOrderController(Controller):
  def perform(self, request):
    try:
      id = request.path.split('/')[-1]
      order = Order.select().where(Order.id == id).execute()
      if order:
        Order.delete().where(Order.id == id).execute()
        order_motorcycles = OrderMotorcycles.select().where(OrderMotorcycles.order == id).execute()
        for item in order_motorcycles:
          motorcycle = Motorcycle.select().where(Motorcycle.id == item.motorcycle).first()
          if motorcycle:
            quantity = motorcycle.quantity + item.quantity
            Motorcycle.update({ Motorcycle.quantity: quantity }).where(Motorcycle.id == item.motorcycle).execute()
        OrderMotorcycles.delete().where(OrderMotorcycles.order_id == id).execute()
        return no_content()
      raise(Exception('Order not found'))
    except Exception as error:
      return bad_request(str(error))