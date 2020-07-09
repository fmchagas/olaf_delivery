# from olaf_delivery.ext.site.main import bp
from .main import bp


def init_app(app):
    return app.register_blueprint(bp)
