from flask import Flask
import os

def setup_routes (app: Flask):
  files = [file for file in os.listdir('main/routes')]
  for file in files:
    if file.endswith('.py') and not file.startswith('__'):
      name = file.replace('.py', '')
      module = __import__(f'main.routes.{name}', fromlist=['route'])
      module.route(app)