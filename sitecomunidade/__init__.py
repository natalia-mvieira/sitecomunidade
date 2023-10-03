from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = '6b5fa2af06361aaff79bd2db591de150'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sitecomunidade.db"

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "entrar"
login_manager.login_message_category = 'alert-info'

from sitecomunidade import routes