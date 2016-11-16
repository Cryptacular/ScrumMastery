from flask import render_template, url_for

from ScrumMastery import app


@app.route('/')
def index():
    return render_template('index.html', title="Home",
                           heading="Scrum Mastery",
                           introduction=["Scrum Masters + Dev Team = Happiness!",
                                "This is an app designed to help you keep track of all the things you want to keep \
                                track of as a Scrum Master, and stay in touch with your team!"])


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)