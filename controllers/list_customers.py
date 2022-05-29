import math
from controllers import Controller
from infra import *
from helpers import ok

class ListCustomersController(Controller):
  def perform(self, request):
    page = request.args.get("page", default=1, type=int)
    per_page = request.args.get("per_page", default=10, type=int)
    search = request.args.get("search", default='', type=str)
    offset = (page - 1) * per_page
    limit = per_page
    total = Customer.select().where(Customer.name.contains(search) | Customer.email.contains(search)).count()
    customers = Customer.select().where(Customer.name.contains(search) | Customer.email.contains(search)).order_by(Customer.created_at.desc()).limit(limit).offset(offset)
    return ok(list(customers.dicts()), headers={"X-Total-Count": total, 'X-Total-Pages': math.ceil(total / per_page)})