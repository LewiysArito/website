from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class NameForm(FlaskForm):
    name = StringField("Введите ваше имя", validators=[DataRequired()])
    submit = SubmitField("Отправить")