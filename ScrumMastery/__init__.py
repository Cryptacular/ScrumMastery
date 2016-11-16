import os

from flask import Flask, render_template, url_for

app = Flask(__name__)
app.config['DEBUG'] = True

import models
import views