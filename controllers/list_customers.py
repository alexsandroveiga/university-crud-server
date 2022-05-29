import math
from infra import *
from helpers import ok

class ListCustomersController:
  def handle(self, request):
    page = request.args.get("page", default=1, type=int)
    per_page = request.args.get("per_page", default=10, type=int)
    offset = (page - 1) * per_page
    limit = per_page
    total = Customer.select().count()
    customers = Customer.select().order_by(Customer.created_at.desc()).limit(limit).offset(offset)
    return ok(list(customers.dicts()), headers={"X-Total-Count": total, 'X-Total-Pages': math.ceil(total / per_page)})