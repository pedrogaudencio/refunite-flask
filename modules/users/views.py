from flask import Blueprint, render_template
from flask.ext.login import login_required


user_login = Blueprint('user_login', __name__, template_folder='templates')


@user_login.route('/')
@login_required
def index():
    return render_template("index.html")
