# flaskr/__init__.py
# 各種設定を行う
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config
from config import DevelopmentConfig
from sqlalchemy import create_engine

# @login_requiredに対応する処理
login_manager = LoginManager()
# ログインの関数
login_manager.login_view = 'admin.login'
# ログインにリダイレクトした際のメッセージ
login_manager.login_message = 'ログインしてください'

db = SQLAlchemy()
migrate = Migrate()

# SQLiteのEngin
# engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)

from flaskr.models import company, condition, image, industry, manager, occupation, relation

def create_app():
    app = Flask(__name__, static_folder='./admin/static')
    app.config.from_object(Config)
    # 開発環境
    app.config.from_object(DevelopmentConfig)
    # 本番環境
    # app.config.from_object(ProductionConfig)

    from flaskr.admin.views import bp
 
    app.register_blueprint(bp)
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    return app

# def create_app():
#     app = Flask(__name__, static_folder='./admin/static')
#     app.config.from_object(Config)
#     app.config.from_object(DevelopmentConfig)
    
#     from flaskr.admin.views import bp
 
#     app.register_blueprint(bp)
#     db.init_app(app)
#     migrate.init_app(app, db)
#     login_manager.init_app(app)
#     return app