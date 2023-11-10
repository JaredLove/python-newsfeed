from app.routes import home, dashboard

# First, the .home syntax directs the program to find the module named home in the current directory. Next, we want to import the bp object, 
# but we rename it home as part of the import process, for practicality's sake.
from .home import bp as home

from .dashboard import bp as dashboard

# We use a from...import statement to import the Flask() function 
from flask import Flask
# then use the def keyword to define a create_app() function.
# On Windows, run the command $env:FLASK_APP = "app" to set the FLASK_APP variable.
def create_app(test_config=None):
# set up app config
# The app should serve any static resources from the root directory and not from the default /static directory.
# Trailing slashes are optional (meaning that /dashboard and /dashboard/ load the same route).
# The app should use the key called 'super_secret_key' when creating server-side sessions.
    app = Flask(__name__, static_url_path='/')
    app.url_map.strict_slashes = False
    app.config.from_mapping(
        SECRET_KEY='super_secret_key'
    )
# register blueprints
    @app.route('/hello')
    def hello():
        return 'hello world'
    # register routes
    app.register_blueprint(home)
    app.register_blueprint(dashboard)

    return app