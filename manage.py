from ScrumMastery import app
from flask_script import Manager
app.config['SECRET_KEY'] = '\xcf3\xc3f\xda\x14\xf7)\xf1p\x10t\xc2}\xdb\x91dF%\xbe\xe9t\x89\x03'

manager = Manager(app)

if __name__ == '__main__':
    manager.run()