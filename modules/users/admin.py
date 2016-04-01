from wtforms.fields import PasswordField

from flask.ext.admin.base import MenuLink
from flask.ext.admin.contrib import sqla
from flask.ext.login import current_user
from flask.ext.security.utils import encrypt_password


class UserAdmin(sqla.ModelView):
    # Exclude the password field from the user list
    column_exclude_list = ('password',)
    form_excluded_columns = ('password',)
    column_auto_select_related = True

    def is_accessible(self):
        return current_user.has_role('admin')

    def scaffold_form(self):
        """On the form for creating or editing a User, we don't display a field
        corresponding to the model's password field. We want to encrypt the
        password before storing in the database and we want to use a password
        field (with the input masked) rather than a regular text field.

        We start with the standard form as provided by Flask-Admin and we
        exclude the password field from this form.
        """
        form_class = super(UserAdmin, self).scaffold_form()
        form_class.password2 = PasswordField('New Password')
        return form_class

    def on_model_change(self, form, model, is_created):
        if len(model.password2):
            model.password = encrypt_password(model.password2)


# Customized Role model for SQL-Admin
class RoleAdmin(sqla.ModelView):
    def is_accessible(self):
        return current_user.has_role('admin')


# -------
# Helpers
# -------

class AuthenticatedMenuLink(MenuLink):
    def is_accessible(self):
        return current_user.is_authenticated


class NotAuthenticatedMenuLink(MenuLink):
    def is_accessible(self):
        return not current_user.is_authenticated
