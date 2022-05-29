class ServerError(Exception):
  def __init__(self, message='Server failed. Try again soon'):
    self.message = message
    super().__init__(self.message) 

def ok(data, headers=None):
  return {
    "statusCode": 200,
    "data": data,
    "headers": headers
  }

def bad_request(error, headers=None):
  return {
    "statusCode": 400,
    "data": error,
    "headers": headers
  }

def no_content():
  return {
    "statusCode": 201,
    "data": None,
    "headers": None
  }

def server_error():
  return {
    "statusCode": 500,
    "data": ServerError(),
    "headers": None
  }