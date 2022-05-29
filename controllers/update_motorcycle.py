from infra import *
from helpers import *
from controllers import Controller

class UpdateMotorcycleController(Controller):
  def perform(self, request):
    try:
      id = request.path.split('/')[-1]
      motorcycle = Motorcycle.select().where(Motorcycle.id == id)
      if motorcycle:
        print(motorcycle)
        Motorcycle.update(**request.json).where(Motorcycle.id == id).execute()
        return ok(Motorcycle.get_by_id(id).__data__)
      raise(Exception('Motorcycle not found'))
    except Exception as error:
      return bad_request(str(error))