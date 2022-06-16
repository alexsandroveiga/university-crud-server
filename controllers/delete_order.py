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
        return no_content()
      raise(Exception('Order not found'))
    except Exception as error:
      return bad_request(str(error))