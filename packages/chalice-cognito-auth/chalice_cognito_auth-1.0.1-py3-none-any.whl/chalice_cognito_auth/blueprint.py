import os
import sys

from chalice import Blueprint

from chalice_cognito_auth.exceptions import InvalidAuthHandlerNameError
from chalice_cognito_auth.utils import get_param
from chalice_cognito_auth.utils import handle_client_errors


class BlueprintFactory:
    def _rename_fn(self, name):
        def renamer(fn):
            def wrapped(*args, **kwargs):
                return fn(*args, **kwargs)
            wrapped.__name__ = name
            return wrapped
        return renamer


    def create_blueprint(self, name, authorizer, lifecycle):
        if name in vars(sys.modules[__name__]):
            raise InvalidAuthHandlerNameError(name)

        routes = Blueprint('%s' % __name__)

        @routes.authorizer(name=name)
        @self._rename_fn(name)
        def auth(auth_request):
            return authorizer.auth_handler(auth_request)

        @routes.route('/login', methods=['POST'])
        @handle_client_errors
        def login():
            body = routes.current_request.json_body
            username = get_param(body, 'username', required=True)
            password = get_param(body, 'password', required=True)
            return lifecycle.login(username, password)

        @routes.route('/logout', methods=['POST'],
                      authorizer=auth)
        @handle_client_errors
        def logout():
            body = routes.current_request.json_body
            access_token = get_param(body, 'access_token', required=True)
            lifecycle.logout(access_token)
            return 'success'

        @routes.route('/refresh', methods=['POST'])
        @handle_client_errors
        def refresh():
            body = routes.current_request.json_body
            id_token = get_param(body, 'id_token', required=True)
            refresh_token = get_param(body, 'refresh_token', required=True)
            access_token = get_param(body, 'access_token', required=True)
            return lifecycle.refresh(id_token, refresh_token, access_token)

        setattr(sys.modules[__name__], name, auth)
        return routes, auth


def _import_chalice_app_if_needed():
    # Chalice isn't loaded in an authorizer because the lambda handler string
    # does not load the app.* file. It loads chalice_cognito_auth.blueprint.*
    # instead. This causes create_blueprint not to get called (since it is
    # called in app.py) and hence it prevents the authorizer handler function
    # from getting injected into this module. This method is called on module
    # load to include app.py (hence calling create_blueprint) and preventing
    # a circular import.
    if 'app' in sys.modules:
        return
    import app


if os.environ.get("AWS_EXECUTION_ENV") is not None:
    _import_chalice_app_if_needed()
