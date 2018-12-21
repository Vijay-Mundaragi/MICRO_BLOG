from flask import Blueprint

bp = Blueprint("main", __name__)

from my_app.errors import handlers
