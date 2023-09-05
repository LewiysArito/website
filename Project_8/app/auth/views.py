from app.auth import auth
from flask import render_template, redirect, url_for, flash, request
from app.models import User, db
from app.auth.forms import LoginForm, RegisterForm, ValidationError
from flask_login import login_user, logout_user, login_required


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_btn.data)
            '''login_user регистрирует пользователя в сессии, второй аргумент запоминает данного пользователя даже после перезагрузки сайт,
            если чекбокс показывает True, иначе показывает значение False
            '''
            if request.args.get("next"):
                return redirect(request.args.get("next"))
                '''аргументы запроса, если есть аргумент next, то переадресирует на next, если его нет,
                то на главную страницу'''
            return redirect(url_for("main.index"))
        flash("Неправильный логин или пароль")
    return render_template("auth/login.html", form=form)
    "в данном случае сенс пользователя сохраняется , а значение True сохраняет значения в куках" \
    "браузера пользователя, из-за чего он может перезайти заново на сайт с сохранёнными данными , с помощью чего" \
    "можно будет предотвратить прерванный сеанс"


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Вы вышли со своего аккаунта")
    return redirect(url_for("main.index"))


@auth.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        try:
            form.validate_username(form.username)
            form.validate_email(form.email)
            user = User(email=form.email.data,
                        username=form.username.data,
                        password=form.password.data)
            db.session.add(user)
            flash("Вы успешно зарегистрировались")
            return redirect(url_for("auth.login"))
        except ValidationError:
            return redirect(url_for("auth.register"))

    return render_template("auth/register.html", form=form)
