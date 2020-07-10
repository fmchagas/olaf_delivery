# from olaf_delivery.ext.site.main import bp
from flask_debugtoolbar import DebugToolbarExtension


def init_app(app):
    DebugToolbarExtension(app)
