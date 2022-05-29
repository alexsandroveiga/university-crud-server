from infra import *
from helpers import *
from controllers import Controller

class UpdateCustomerController(Controller):
  def perform(self, request):
    try:
      id = request.path.split('/')[-1]
      customer = Customer.select().where(Customer.id == id)
      if customer:
        Customer.update(**request.json).where(Customer.id == id).execute()
        return ok(Customer.get_by_id(id).__data__)
      raise(Exception('Customer not found'))
    except Exception as error:
      return bad_request(str(error))