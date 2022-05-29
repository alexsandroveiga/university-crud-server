from infra import *
from helpers import *

class DeleteCustomerController:
  def handle(self, request):
    Customer.delete_by_id(request.path.split('/')[-1])
    return no_content()