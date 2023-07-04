# flaskr/__init__.py
# 各種設定を行う
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config
from config import DevelopmentConfig
from flaskr.admin.views import bp

# @login_requiredに対応する処理
login_manager = LoginManager()
# ログインの関数
login_manager.login_view = 'admin.login'
# ログインにリダイレクトした際のメッセージ
login_manager.login_message = 'ログインしてください'

basedir = os.path.abspath(os.path.dirname(__name__))
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config.from_object(DevelopmentConfig)

    app.register_blueprint(bp)
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    return app

# def create_app():
#     app = Flask(__name__)
#     from flaskr.admin.views import admin_bp
#     from flaskr.recruit.views import recruit_bp

#     app.register_blueprint(admin_bp)
#     app.register_blueprint(recruit_bp)
#     return app