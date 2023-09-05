import psycopg2
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from app import login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))  # возвращает объект пользователя из бд


'''данный декоратор связывает функцию аутентификации login_manager
c loaduser и говорит, как их загружать 
'''


class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    users = db.relationship("User", backref="role", lazy="dynamic")

    def __repr__(self):
        return f"<Role {self.name}>"


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, index=True)
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))

    @property
    def password(self):  # это геттер
        raise AttributeError("password is not readeble attribute")

    '''позволяет локальным переменным, гетеррировать и сеттерировать их более удобным образом,
    после чего к ним можно обращаться через свойство password 
    в этом случае геттер является объектом свойством для выполнения, считывания содержимого функции
    например создав экземпляр класса пользователя с именем user_nikita
    обращение к паролю будет выглядеть следующим образом 
    print(user_nikita.password) инициирует ошибку
    на основе хеша нельзя восстановить оригинальный пароль
    '''

    "имена функций сеттеров и геттеров должны совпадать"

    @password.setter  # это сеттер
    def password(self, password):
        self.password_hash = generate_password_hash(password)  # генерирует хеш на основе пароля

    # @password.deleter  # это делитер, вдруг пригодится
    # def password(self, password):
    #     self.password_hash = None

    def verify_password(self, password):
        return check_password_hash(self.password_hash,
                                   password)  # возвращает True, если пароль совпадает с хешем, сохранённым в бд

    def __repr__(self):
        return f"< User {self.username}>"
