import os

from app import create_app


if __name__ == "__main__":
    os.environ["FLASK_DEBUG"] = "1"
    application = create_app()
    application.run(debug=True)
else:
    gunicorn_app = create_app()
