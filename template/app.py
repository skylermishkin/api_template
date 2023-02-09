import logging
from os import mkdir

from flask import Flask

from template import APP_DIR, SERVICE_NAME
from template.views import base_blueprint

# Setup a nice lil logger
log_dir = f"{APP_DIR}/logs"
try:
    mkdir(log_dir)
except FileExistsError:
    pass
log_handler = logging.FileHandler(f"{log_dir}/template_app.log")
log_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - [%(levelname)s] : %(message)s"
)
log_handler.setFormatter(log_formatter)
logger = logging.getLogger(SERVICE_NAME)
logger.setLevel("INFO")
logger.addHandler(log_handler)


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(base_blueprint)
    return app
