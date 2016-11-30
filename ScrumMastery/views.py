from datetime import datetime
from flask import render_template, url_for, request, redirect

from ScrumMastery import app

accounts = []


def create_new_account(email, password):
    accounts.append(dict(
        email = email,
        password = password,
        created = datetime.utcnow()
    ))
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
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        create_new_account(email, password)
        return redirect(url_for('index'))

    return render_template('create_account.html',
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