from flask import Flask
from config import app_config


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(app_config[config_filename])

    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api/v1')

    return app

if __name__=="__main__":
    app = create_app("development")
    app.run(debug=True)