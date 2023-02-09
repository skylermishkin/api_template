from flask import Blueprint

base_blueprint = Blueprint("base_blueprint", __name__)


@base_blueprint.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
