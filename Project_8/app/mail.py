from flask_mail import Message
from app import mail
from flask import render_template, current_app
from threading import Thread
def send_async_email(cur_app, cur_msg):
    with cur_app.app_context():
        mail.send(cur_msg)


def send_email(to, subject, template,
               **kwargs):
    app = current_app._get_current_object()
    msg = Message(app.config["FLASK_MAIL_SUBJECT_PREFIX"] + " " + subject,
                  sender=app.config["FLASK_MAIL_SENDER"], recipients=[to])
    msg.body = render_template(template + ".txt", **kwargs)
    msg.html = render_template(template + ".html", **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr