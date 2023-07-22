from dotenv import load_dotenv
load_dotenv(override=True)
import os
env_path = os.path.join(os.path.dirname(__file__), 'secrets/.env.dev')
load_dotenv(env_path)

basedir = os.path.abspath(os.path.dirname(__name__))

# デフォルト
class Config:
    FLASK_DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv("SECRET_KEY")
    # SQLite用
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    # PostgreSQL用
    POSTGRES_HOST = os.getenv("POSTGRES_HOST")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT")
    POSTGRES_DB = os.getenv("POSTGRES_DB")
    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")

    SQLALCHEMY_DATABASE_URI = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# 本番環境
class ProductionConfig(Config):
    pass

# 開発環境
class DevelopmentConfig(Config):
    FLASK_DEBUG = os.getenv("FLASK_DEBUG")
    SQLALCHEMY_ECHO = os.getenv("SQLALCHEMY_ECHO")

class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False

config = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig,

    'default': DevelopmentConfig
    }