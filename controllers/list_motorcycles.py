import math
from flask import Request
from infra import *
from helpers import ok
from controllers import Controller

class ListMotorcyclesController(Controller):
  def perform(self, request: Request):
    page = request.args.get("page", default=1, type=int)
    per_page = request.args.get("per_page", default=10, type=int)
    search = request.args.get("search", default='', type=str)
    offset = (page - 1) * per_page
    limit = per_page
    total = Motorcycle.select().where(Motorcycle.brand.contains(search) | Motorcycle.model.contains(search)).count()
    motos = Motorcycle.select().where(Motorcycle.brand.contains(search) | Motorcycle.model.contains(search)).order_by(Motorcycle.created_at.desc()).limit(limit).offset(offset)
    return ok(list(motos.dicts()), headers={"X-Total-Count": total, 'X-Total-Pages': math.ceil(total / per_page)})