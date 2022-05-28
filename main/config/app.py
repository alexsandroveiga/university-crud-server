from flask import Flask
from flask_cors import CORS
from .routes import setup_routes

app = Flask(__name__)
CORS(app, expose_headers=['X-Total-Count', 'X-Total-Pages'])
app.config.from_object(__name__)

setup_routes(app)