from flask import Flask

from config import app_config
from app.api.v2.models.db import init_db

from app.api.v2.views.users import version2 as userspath
from app.api.v2.views.books import version2 as bookspath

def create_app(config_name):
    app = Flask(__name__)
    app.url_map.strict_slashes = False  # disable strict slashes
    app.config.from_object(app_config[config_name])
    app.register_blueprint(userspath)
    app.register_blueprint(bookspath)
    init_db(app_config["DB_URL"])
    return app