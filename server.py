from main.config.app import app
from infra.entities import create_tables

if __name__ == '__main__':
  app.debug = True
  create_tables()
  app.run(host='0.0.0.0')
  print('Running on http://localhost:5000')