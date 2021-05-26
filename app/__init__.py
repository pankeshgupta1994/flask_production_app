from flask import Flask
from config import config
import os

app_config = config[os.getenv('APP_ENV') or 'default']
UPLOAD_FOLDER = os.path.dirname(os.path.dirname(__file__)+'/upload/')
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def create_app(configuration):
    app = Flask(__name__)
    app.config.from_object(config[configuration])
    config[configuration].init_app(app)
    app.secret_key = os.urandom(24)

    from .upload import uploads as uploads_blueprint
    app.register_blueprint(uploads_blueprint)
    return app