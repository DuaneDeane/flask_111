#!/user/bin/env python3
# -*- coding: utf8 -*-
""" Simple database operations """

from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.config["SECRET KEY"] = "MYSUPERSECRETSTRING"

from app import routes