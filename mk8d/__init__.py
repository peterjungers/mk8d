from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
app.config['SQLALCHEMY_ECHO'] = False
db = SQLAlchemy(app)

from mk8d import handlers
from mk8d import models
from mk8d import routes


