from datetime import datetime
from flask import render_template, url_for, request, redirect, flash

from ScrumMastery import app
from manage import db
from models import User
from forms import CreateAccountForm


def create_new_account(email, password):
    user = User(email=email, password=password)
    db.session.add(user)
    db.session.commit()
    return


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title="Home",
                           heading="Scrum Mastery",
                           introduction=["Scrum Masters + Dev Team = Happiness!",
                                "This is an app designed to help you keep track of all the things you want to keep \
                                track of as a Scrum Master, and stay in touch with your team!"])


@app.route('/create-account', methods=['GET', 'POST'])
def create_account():
    form = CreateAccountForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        create_new_account(email, password)
        flash("Account for {} created, please log in!".format(email))
        return redirect(url_for('index'))

    return render_template('create_account.html',
                           form=form,
                           title="Create Account",
                           heading="Create an Account",
                           introduction=["Create an account and be like brah, yo.", accounts])


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)