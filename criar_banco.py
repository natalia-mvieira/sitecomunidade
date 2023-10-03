from sitecomunidade import database, app
from sitecomunidade.models import Usuario, Post

with app.app_context():
    database.create_all()