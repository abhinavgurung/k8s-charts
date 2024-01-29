from app.config import DevelopmentConfig, TestConfig, ProductionConfig, UnitTestConfig

from flask import Flask, request, g, jsonify
import os,sys
import logging
import logging.config

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from flask_cors import CORS
port = '11211'
host = 'memcached'
memcached_uri = f'memcached://{host}:{port}'
limiter = Limiter(storage_uri=memcached_uri, key_func=get_remote_address)

def create_app():
    app = Flask(__name__)

    config = get_environment_config()

    limiter.init_app(app)
    app.config.from_object(config)


    # cors = CORS(app, origins=config.CORS_ORIGINS)
    CORS(app)

    
    # Register blueprints
    register_blueprints(app)

    @app.route('/echo')
    def hello():
        return 'Hello, World!'

    @app.route("/test2", methods=["GET"])
    def get_test():
        logging.warning("got api request new...........")
        info = {
            "school" : 'Federal University Of Technology Owerri',
            "department" : "Biochemistry",
            'level': "500L"
        }
        return jsonify(info) # returning a JSON response

    return app




def get_environment_config():
    """Get the environment-specific config the app should use."""
    # environment variable encodes both env and channel, we only care about the env.
    portal_env = os.environ.get("PORTAL_ENV") or "Local-development"
    environment = portal_env.split("-")
    env = environment[0]

    logging.info(f"Getting environment config from: {environment}")

    if env == "Production":
        return ProductionConfig
    elif env == "Test":
        return TestConfig
    elif env == "Development":
        return DevelopmentConfig
    elif env == "UnitTest":
        return UnitTestConfig
    else:
        logging.info(
            "PORTAL_ENV not recognized or not provided - defaulting to local/dev configuration.")
        return DevelopmentConfig


def register_blueprints(app):
    """Register the application's blueprints"""
    from app.api.requests import requests_view
    
    app.register_blueprint(requests_view)