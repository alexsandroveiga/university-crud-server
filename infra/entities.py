import peewee
from peewee import *
from uuid import uuid4

DATABASE = 'infra/database.db'
database = SqliteDatabase(DATABASE)

class BaseModel(Model):
  class Meta:
    database = database

class Customer(BaseModel):
  class Meta:
    table_name = 'customers'

  id = CharField(primary_key=True, default=uuid4)
  name = CharField()
  email = CharField(unique=True)
  gender = CharField()
  identifier = CharField()
  address = CharField()
  phone = CharField()
  state = CharField()
  city = CharField()
  zip_code = CharField()
  avatar_url = CharField()
  created_at = DateTimeField(default=peewee.datetime.datetime.now)
  updated_at = DateTimeField(default=peewee.datetime.datetime.now)

class Motorcycle(BaseModel):
  class Meta:
    table_name = 'motorcycles'

  id = CharField(primary_key=True, default=uuid4)
  brand = CharField()
  model = CharField()
  price = FloatField()
  engine_capacity = IntegerField()
  maximum_power = IntegerField()
  image_url = CharField()
  quantity = IntegerField()
  created_at = DateTimeField(default=peewee.datetime.datetime.now)
  updated_at = DateTimeField(default=peewee.datetime.datetime.now)

class Order(BaseModel):
  class Meta:
    table_name = 'orders'

  id = CharField(primary_key=True, default=uuid4)
  customer = ForeignKeyField(Customer, backref='orders')
  created_at = DateTimeField(default=peewee.datetime.datetime.now)
  updated_at = DateTimeField(default=peewee.datetime.datetime.now)

class OrderMotorcycles(BaseModel):
  class Meta:
    table_name = 'orders_motorcycles'

  id = CharField(primary_key=True, default=uuid4)
  order = ForeignKeyField(Order, backref='order_products')
  motorcycle = ForeignKeyField(Motorcycle, backref='order_products')
  quantity = IntegerField()
  price = FloatField()
  created_at = DateTimeField(default=peewee.datetime.datetime.now)
  updated_at = DateTimeField(default=peewee.datetime.datetime.now)

def create_tables():
  with database:
    database.create_tables([Customer, Motorcycle, Order, OrderMotorcycles])

