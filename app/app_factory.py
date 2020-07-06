from flask import Flask
from .extensions import bootstrap, auth, ma
from .config import ConfigClass
from .models import db
from .views.api_routes import api_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object(ConfigClass)
    app.url_map.strict_slashes = False
    
    db.init_app(app)
    ma.init_app(app)
    auth.init_app(app)
    bootstrap.init_app(app)

    app.register_blueprint(api_blueprint)

    @app.errorhandler(404)
    def page_not_found(e):
        return "<html><h1>Ain't no page around here by that name.</html></h1>", 404
    
    return app
