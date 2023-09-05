from datetime import datetime
from flask import render_template, session, redirect, url_for, current_app
from app.main import main_blueprint
from app.main.forms import NameForm
from app.mail import send_email
from app.models import db
from app.models import User


@main_blueprint.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")