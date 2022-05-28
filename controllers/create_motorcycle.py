from infra import *
from helpers import ok

class CreateMotorcycleController:
  def handle(self, request):
    return ok(Motorcycle.create(**request.json).__data__)