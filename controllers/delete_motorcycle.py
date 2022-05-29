from infra import *
from helpers import *

class DeleteMotorcycleController:
  def handle(self, request):
    Motorcycle.delete_by_id(request.path.split('/')[-1])
    return no_content()