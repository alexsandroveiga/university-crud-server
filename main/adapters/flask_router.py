from flask import *
from json import *

def adapt_flask_route(controller):
  response = controller.handle(request)
  if (response['statusCode'] == 200):
    json = response['data']
  else:
    json = { 'error': response['data'] }
  return Response(dumps(json, default=str), mimetype='application/json', status=response['statusCode'], headers=response['headers'])