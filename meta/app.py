#coding: utf-8

import os
from flask import Flask


here = os.path.dirname(os.path.abspath(__file__))


def build(config=None):
    app = Flask(__name__)

    app.config.from_pyfile(os.path.join(here, 'conf/basic.py'))
    if isinstance(config, dict):
        app.config.update(config)
    elif isinstance(config, str):
        app.config.from_pyfile(config)

    return app
