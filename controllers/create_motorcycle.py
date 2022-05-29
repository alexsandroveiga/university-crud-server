from infra import *
from controllers import Controller
from helpers import ok

class CreateMotorcycleController(Controller):
  def perform(self, request):
    return ok(Motorcycle.create(**request.json).__data__)