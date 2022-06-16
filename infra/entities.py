import peewee
from peewee import *
from uuid import uuid4

### Using SQLite3 as the database
# DATABASE = 'infra/database.db'
# database = SqliteDatabase(DATABASE)

### Using PostgreSQL as the database
database = PostgresqlDatabase('da8s5g3ar1it5v', user='wwcivpdmtpwrug', host='ec2-52-72-99-110.compute-1.amazonaws.com', port=5432, password='3e5a59c23d921f56a8a2815fe060f5613445bec58937de380ccb590a52e5b2c9')

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

