from flask import Blueprint

bp = Blueprint('questions', __name__)

from questions import routes
