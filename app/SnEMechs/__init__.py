from flask import Blueprint

SnEMechs = Blueprint('SnEMechs', __name__)

from . import views, errors  # noqa
