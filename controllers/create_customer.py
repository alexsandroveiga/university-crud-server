from infra import *
from helpers import ok

class CreateCustomerController:
  def handle(self, request):
    return ok(Customer.create(**request.json).__data__)