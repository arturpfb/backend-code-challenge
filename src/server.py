import re

from flask import Flask, request
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from prometheus_client import make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware

from logger import LOGGER
from config import APP_NAME, SQLALCHEMY_DATABASE_URI, PORT, DEBUG

from api.healthcheck import healthcheck_blueprint


def setup_migrations(app):
    uri = SQLALCHEMY_DATABASE_URI
    app_name = APP_NAME

    connection_string_last_piece = uri.split("/")[-1]
    connection_string_already_has_options = bool(
        re.search("\?", connection_string_last_piece)
    )
    complete_connection_string = (
        uri
        + ("&" if connection_string_already_has_options else "?")
        + f"application_name={app_name}"
    )

    app.config["SQLALCHEMY_DATABASE_URI"] = complete_connection_string
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    return SQLAlchemy(app)


def setup_app():
    app = Flask(__name__)

    # Add prometheus wsgi middleware to route /metrics requests
    app.wsgi_app = DispatcherMiddleware(
        app.wsgi_app, {"/metrics": make_wsgi_app()}
    )

    return app


app = setup_app()

db = setup_migrations(app)
migrate = Migrate(app, db)

CORS(app)


@app.route("/server_request")
def server_request():
    print(request.args.get("param"))
    return "served"


def register_blueprints(app):
    LOGGER.info("Registering blueprints")

    url_prefix = f"/api/v1/{APP_NAME}"

    # by our standards, the healthcheck endpoint does not need a prefix
    # but for template purposes, this is how your regular blueprint should look
    app.register_blueprint(healthcheck_blueprint(), url_prefix=url_prefix)
    # simply remove the param from the healthcheck blueprint and add it to
    # your other endpoints


def run_server():
    port = PORT
    debug = DEBUG

    register_blueprints(app)

    app.run(host="0.0.0.0", debug=debug, threaded=False, port=port)
