from infra import *
from helpers import *
from controllers import Controller

class DeleteCustomerController(Controller):
  def perform(self, request):
    try:
      id = request.path.split('/')[-1]
      customer = Customer.select().where(Customer.id == id).execute()
      if customer:
        Customer.delete().where(Customer.id == id).execute()
        return no_content()
      raise(Exception('Customer not found'))
    except Exception as error:
      return bad_request(str(error))