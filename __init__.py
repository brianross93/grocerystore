from flask import Flask
from flask_login import LoginManager
from grocery_app.models import User
from flask_bcrypt import Bcrypt

app = Flask(__name__)

login_manager = LoginManager()
bcrypt = Bcrypt(app)

@login_manager.user_loader
def load_user(user_id):
   return User.query.get(user_id)