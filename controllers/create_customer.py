from infra import *
from controllers import Controller
from helpers import *

class CreateCustomerController(Controller):
  def perform(self, request):
    try:
      customer = Customer.select().where(Customer.email == request.json['email']).execute()
      if customer:
        raise(Exception('Customer already exists'))
      return ok(Customer.create(**request.json).__data__)
    except Exception as error:
      return bad_request(str(error))