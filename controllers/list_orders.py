import math

from django.forms import model_to_dict
from controllers import Controller
from infra import *
from helpers import *

from playhouse.shortcuts import model_to_dict

class ListOrdersController(Controller):
  def perform(self, request):
    query = Order.select().order_by(Order.created_at.desc())
    orders = [model_to_dict(order, backrefs=True) for order in query]
    return ok(list(orders))