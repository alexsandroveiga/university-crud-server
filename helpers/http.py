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

def serverError():
  return {
    "statusCode": 500,
    "data": ServerError()
  }