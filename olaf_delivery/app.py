from flask import Flask
from olaf_delivery.ext import site
from olaf_delivery.ext import config
from olaf_delivery.ext import toolbar
from olaf_delivery.ext import db
from olaf_delivery.ext import cli


def create_app():
    """Factory principal"""
    app = Flask(__name__)

    config.init_app(app)
    db.init_app(app)
    cli.init_app(app)
    toolbar.init_app(app)
    site.init_app(app)
    return app
