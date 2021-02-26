from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from grocery_app.config import Config
import os
import flask_login
from .models import User
from flask.ext.bcrypt import Bcrypt





app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config.from_object(Config)
app.secret_key = os.urandom(24)

db = SQLAlchemy(app)



from grocery_app.routes import main

app.register_blueprint(main)

with app.app_context():
    db.create_all()

login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
   return User.query.get(user_id)
