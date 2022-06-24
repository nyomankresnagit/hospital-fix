from flask_login import login_required, current_user, login_user, logout_user
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import DevelopmentConfig
import os
import pandas as pd
from io import BytesIO
from pathlib import Path
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash

# This file work for initialize projects that will run on the website.

# This code work for calling library Flask-SQLAlchemy to use the function inside that library.
db = SQLAlchemy()

# This code work for calling library Flask-Migrate to use the function inside that library.
migrate = Migrate()

# The code below work for running main app with Flask framework using configuration from file config.py.
# This code also register the blueprint from other folder / file.
def create_app(config=DevelopmentConfig):
    app_hospital = Flask(__name__)
    app_hospital.config.from_object(config)

    mysql = MySQL(app_hospital)
    mysql.app_hospital = app_hospital

    db.init_app(app_hospital)
    db.app_hospital = app_hospital

    migrate.init_app(app_hospital, db)
    migrate.app_hospital = app_hospital

    login_manager = LoginManager()
    login_manager.init_app(app_hospital)

    from app_hospital.auth.model_auth import auth
    @login_manager.user_loader
    def load_user(id_auth):
        return auth.query.get(int(id_auth))

    from app_hospital.admin import admin_bp
    app_hospital.register_blueprint(admin_bp)

    from app_hospital.admin_history import admin_history_bp
    app_hospital.register_blueprint(admin_history_bp)

    from app_hospital.auth import auth_bp
    app_hospital.register_blueprint(auth_bp)

    from app_hospital.dashboard import dashboard_bp
    app_hospital.register_blueprint(dashboard_bp)

    from app_hospital.dokter import dokter_bp
    app_hospital.register_blueprint(dokter_bp)

    from app_hospital.dokter_history import dokter_history_bp
    app_hospital.register_blueprint(dokter_history_bp)

    from app_hospital.pasien import pasien_bp
    app_hospital.register_blueprint(pasien_bp)

    from app_hospital.pasien_history import pasien_history_bp
    app_hospital.register_blueprint(pasien_history_bp)

    from app_hospital.trans import trans_bp
    app_hospital.register_blueprint(trans_bp)

    return app_hospital