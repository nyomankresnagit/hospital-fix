from flask import Blueprint

auth_bp = Blueprint('auth_bp', __name__, template_folder='templates', static_folder='static')

from app_hospital.auth import view_auth