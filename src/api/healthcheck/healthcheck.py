import flask

from datetime import datetime
from flask.views import MethodView

from services import Postgres
from pool import backend_code_challenge_pool


class HealthCheck(MethodView):
    """A healthcheck endpoint, used to monitor the health of this app."""

    def get(self):
        is_codechallenge_db_healthy = Postgres(
            backend_code_challenge_pool
        ).health_check()

        healthy = "db is healthy"
        unhealthy = "db is unhealthy, database connection error"

        message = {
            "backend_code_challenge_db": f"{healthy if is_codechallenge_db_healthy else unhealthy}"
        }

        return {
            "host": flask.request.host,
            "timestamp": datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f"),
            "message": message,
        }
