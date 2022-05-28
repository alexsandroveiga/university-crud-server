import peewee
from peewee import *
from uuid import uuid4

#db = PostgresqlDatabase('database', user='postgres', host='localhost', port=5432, password='docker')

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
  price = CharField()
  engine_capacity = CharField()
  maximum_power = CharField()
  image_url = CharField()
  created_at = DateTimeField(default=peewee.datetime.datetime.now)
  updated_at = DateTimeField(default=peewee.datetime.datetime.now)

def create_tables():
  with database:
    database.create_tables([Customer, Motorcycle])