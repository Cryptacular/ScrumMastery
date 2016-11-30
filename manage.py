import os

from ScrumMastery import app
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SECRET_KEY'] = '\xcf3\xc3f\xda\x14\xf7)\xf1p\x10t\xc2}\xdb\x91dF%\xbe\xe9t\x89\x03'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'scrum_mastery.db')
db = SQLAlchemy(app)

manager = Manager(app)

if __name__ == '__main__':
    manager.run()