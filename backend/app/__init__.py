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

    # Setup logging (should be done first before anything else so logging can apply to all subsequent code)
    # setup_logging(app)

    

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
    
def setup_logging(app):
    """Initialize the logging setup for the application."""
    # Disable the default flask (werkzeug) response logging.
    logging.getLogger("werkzeug").setLevel(logging.WARN)

    @app.before_request
    def before_request():
        """Assign request-scoped variables to the request context for use by the request."""
        g.request_id = uuid.uuid4()
        g.locale = request.accept_languages.best_match(["en", "fr"], "en")

    @app.after_request
    def after_request(response):
        """After each request, log the relevant details (time/method/response status)"""
        logging.info(
            "{ip} - {method} {path} {version} - {status_code}".format(
                ip=request.remote_addr,
                method=request.method,
                path=request.path,
                version=request.environ.get("SERVER_PROTOCOL"),
                status_code=response.status_code)
        )

        return response

    logging.root.setLevel("INFO")

    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s [%(name)s] [%(threadName)s] [request_id=%(request_id)s] [upn=%(upn)s] %(pathname)s.%(funcName)s(%(filename)s:%(lineno)d) - %(message)s")

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    console_handler.addFilter(RequestIDLogFilter())

    file_handler = TimedRotatingFileHandler(
        'app.log', when="d", interval=1, backupCount=30)
    file_handler.setFormatter(formatter)
    file_handler.addFilter(RequestIDLogFilter())

    logging.getLogger().addHandler(console_handler)
    logging.getLogger().addHandler(file_handler)