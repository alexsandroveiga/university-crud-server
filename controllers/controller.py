from helpers import *

class Controller:
  def handle (self, request):
    try:
      return self.perform(request)
    except:
      return server_error()