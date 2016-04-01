import os

from flask import Flask
from flask.ext.security import (
    Security,
    SQLAlchemyUserDatastore,
)
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# --------------------
# Modules & extensions
# --------------------

# Users & Roles
from modules.users.models import User, Role
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

# Blueprint registration
from modules.users.views import user_login
app.register_blueprint(user_login)
