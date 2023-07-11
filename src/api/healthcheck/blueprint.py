"""
Blueprint.

Blueprint é o módulo que define os blueprints para as rotas de health-check
"""
from flask import Blueprint

from .healthcheck import HealthCheck


def healthcheck_blueprint():
    """Retorna a blueprint de healthcheck."""
    blueprint = Blueprint("healthcheck", __name__)

    blueprint.add_url_rule(
        "/healthcheck", view_func=HealthCheck.as_view("healthcheck")
    )

    return blueprint
