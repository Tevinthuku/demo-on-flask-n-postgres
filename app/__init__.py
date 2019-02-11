from flask import Flask

from config import app_config
from app.api.v2.models.db import init_db

from app.api.v2.views.users import version2 as userspath

def createApp(config_name):
    app = Flask(__name__)
    app.url_map.strict_slashes = False  # disable strict slashes
    app.config.from_object(app_config[config_name])
    app.register_blueprint(userspath)
    init_db(app_config["DB_URL"])
    return app