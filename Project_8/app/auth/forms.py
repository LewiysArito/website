from wtforms.validators import DataRequired, Email, Length, Regexp, EqualTo, ValidationError
from flask_wtf import FlaskForm
from wtforms import SubmitField, EmailField, PasswordField, BooleanField, StringField
from app.models import User

'для класса Email необходима библиотека email_validator установленная в виртуальном окружении'


class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), Length(7, 65), Email()])
    password = PasswordField("Пароль", validators=[DataRequired(), Length(7, 65)])
    remember_btn = BooleanField("Сохранить данные")  # можно использовать чекбокс
    submit = SubmitField("Авторизоваться")


class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Length(7, 65), Email()])

    username = StringField("Имя пользователя", validators=[DataRequired(), Length(5, 45), Regexp(
        r"^[A-Za-z][A-Za-z0-9!.*_]{5,45}$",
        0,
        "Имя пользователя должно иметь первой букву, а также может иметь цифры, буквы а также знаки .*!_"
    )])  # первый символ - буква , потом идёт регулярное выражение, после флаг 0 - говорящий, что будут использоваться регулярные выражения

    password = PasswordField("Пароль", validators=[DataRequired(), Length(7, 100), Regexp(
        r"^(?=.*[a-zA-Z])(?=.*[A-Z])(?=.*\d)(?=.*[^\w\s])(?!.*\s).{7,100}$",
        0,
        "Пароль должен иметь хотя бы 1 цифру, маленькую и большую букву, и один специальный знак, не являющийся пробелом"
        ". И длина пароля от 7 до 100 символов"

    ), EqualTo("password_confirm",
               message="Пароли должны совпадать")])  # специальный валидатор, поторый проверяет совпадение паролей

    '''Первая группирующая конструкция соответствует любому символу ( . ) 0 или более раз (*),
     за которым следует любая из строчных букв ( [a-z]).
      Во второй группе он соответствует любому символу ( . ) 0 или более раз (*),
       за которым следует любая из прописных букв ( [A-Z]).
        Третья группировка соответствует любому символу ( . ) 0 или более раз (*),
         за которым следует любая из цифр от 0 до 9 ( \d ).
          Наконец, четвертая группировка соответствует любому символу ( . ) 0 или более раз (*),
           за которым следует любой из специальных символов ( ^\w\s ) ИЛИ символ подчеркивания [_].
           любой специальный символ не равный пробелу(^\w\s )'''
    password_confirm = PasswordField("Подтверждение пароля", validators=[DataRequired()])
    submit = SubmitField("Зарегистрироваться")

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("Такой email уже зарегистрирован")

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("Такое имя уже зарегистрировано")


