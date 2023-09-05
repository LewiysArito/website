from config import config
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_login import LoginManager

bootstrap = Bootstrap()
mail = Mail()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = "strong" #надежно защищает сессию
login_manager.login_view = "auth.login"#адрес конечной точки аутентификации, так как login находится внутри макета
'''логин менеджер даёт возможность управлять аутентификацией'''

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config.get(config_name))
    bootstrap.init_app(app)
    mail.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    from app.main import main_blueprint
    from app.auth import auth
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth, url_prefix="/auth")
    return app
'''url_prefix - говорит, что все все маршруты макета, будут с префиксом /auth
    маршрут login будет зарегистрирован так /auth/login
'''

'''создание бд скрипт в консоли пайтон вводится
    from app import create_app
    app = create_app("default") - при это должна существовать база данных, которая указана в конфигурации
    from app import db
    ap_con = app.app_context()
    ap_con.push()
    db.create_all()
    from app.models import Role, User
    admin_role = Role(name = "admin")
    mode_role = Role(name = "moderator")
    user_role = Role(name = "User")
    user_john = User(username = "john", role = admin_role)
    user_john.password = "cat"
    user_john.password_hash выводит'pbkdf2:sha256:600000$LPgIoecgQSeXcYXm$c1d9808b8e6514fb197d84d978ff6721cec77148b18b2f56ab775753b492ca54'
    user_john.verify_password("dog") выводит False

    
'''
