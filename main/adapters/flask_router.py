from flask import *
from json import *

def adapt_flask_route(controller):
  response = controller.handle(request)
  if (response['statusCode'] == 200):
    json = dumps(response['data'], default=str)
  elif (response['statusCode'] == 201): 
    json = ''
  else:
    json = dumps({ 'error': response['data'] }, default=str)
  return Response(json, response['statusCode'], response['headers'], content_type='application/json')