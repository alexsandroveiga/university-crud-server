import math
from flask import Request
from infra import *
from helpers import ok
from controllers import Controller

class ListMotorcyclesController(Controller):
  def perform(self, request: Request):
    page = request.args.get("page", default=1, type=int)
    per_page = request.args.get("per_page", default=10, type=int)
    offset = (page - 1) * per_page
    limit = per_page
    total = Motorcycle.select().count()
    motos = Motorcycle.select().order_by(Motorcycle.created_at.desc()).limit(limit).offset(offset)
    return ok(list(motos.dicts()), headers={"X-Total-Count": total, 'X-Total-Pages': math.ceil(total / per_page)})