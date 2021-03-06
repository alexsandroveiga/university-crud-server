from infra import *
from helpers import *
from controllers import Controller

class DeleteMotorcycleController(Controller):
  def perform(self, request):
    try:
      id = request.path.split('/')[-1]
      motorcycle = Motorcycle.select().where(Motorcycle.id == id).execute()
      if motorcycle:
        Motorcycle.delete().where(Motorcycle.id == id).execute()
        return no_content()
      raise(Exception('Motorcycle not found'))
    except Exception as error:
      return bad_request(str(error))