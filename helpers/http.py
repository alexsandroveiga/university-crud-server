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

def no_content():
  return {
    "statusCode": 201,
    "data": None,
    "headers": None
  }

def serverError():
  return {
    "statusCode": 500,
    "data": ServerError()
  }