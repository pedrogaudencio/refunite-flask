import os

from flask import Flask
from flask.ext.admin import Admin
from flask.ext.admin.base import MenuLink
from flask.ext.security import (
    Security,
    SQLAlchemyUserDatastore,
    utils,
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

# Administration
from modules.users.admin import (
    UserAdmin,
    RoleAdmin,
    AuthenticatedMenuLink,
    NotAuthenticatedMenuLink
)
admin = Admin(app)
admin.add_view(UserAdmin(User, db.session))
admin.add_view(RoleAdmin(Role, db.session))
admin.add_link(MenuLink(name='Refunite', url='/'))
admin.add_link(NotAuthenticatedMenuLink(name='Login',
                                        endpoint='security.login'))
admin.add_link(AuthenticatedMenuLink(name='Logout',
                                     endpoint='security.logout'))

# Bundles
from modules.users.bundles import assets
assets.init_app(app)


# Create admin and test user
@app.before_first_request
def create_user():
    db.create_all()
    user_datastore.find_or_create_role(name='admin',
                                       description='Administrator')
    user_datastore.find_or_create_role(name='user',
                                       description='User')

    encrypted_admin_password = utils.encrypt_password('admin')
    encrypted_user_password = utils.encrypt_password('test')
    if not user_datastore.get_user('admin@refunite.org'):
        user_datastore.create_user(email='admin@refunite.org',
                                   password=encrypted_admin_password)
    if not user_datastore.get_user('test@refunite.org'):
        user_datastore.create_user(email='test@refunite.org',
                                   password=encrypted_user_password)

    db.session.commit()

    user_datastore.add_role_to_user('admin@refunite.org', 'admin')
    user_datastore.add_role_to_user('test@refunite.org', 'user')
    db.session.commit()
