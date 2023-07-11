import os

if not os.environ.get("PRODUCTION"):
    from dotenv import load_dotenv

    load_dotenv()

APP_NAME = "backend-code-challenge"

DEBUG = os.environ.get("DEBUG", False)
PORT = os.environ.get("PORT", 4000)

AUTH = {
    "salt": os.environ.get("SALT", "MOCK"),
    "sf_auth_url": os.environ.get("SF_AUTHENTICATOR_URL", "MOCK"),
}

SALESFORCE = {
    "login_url": os.environ.get("SF_LOGIN_URL", "MOCK"),
    "domain_url": os.environ.get("SF_DOMAIN_URL", "MOCK"),
    "api_version": os.environ.get("API_VERS_SF", "MOCK"),
}

SF_AUTH = {
    "client_id": os.environ.get("SALESFORCE_OAUTH_CLIENT_ID", "MOCK"),
    "client_secret": os.environ.get("SALESFORCE_OAUTH_CLIENT_SECRET", "MOCK"),
    "username": os.environ.get("SALESFORCE_USERNAME", "MOCK"),
    "password": os.environ.get("SALESFORCE_PASSWORD", "MOCK"),
    "token": os.environ.get("SALESFORCE_SECURITY_TOKEN", "MOCK"),
}

PGSQL = {
    "backend_code_challenge_conn": os.environ.get("DATABASE_URL", "MOCK"),
    "minconn": int(os.environ.get("DATABASE_POOL_MINCONN", "1")),
    "maxconn": int(os.environ.get("DATABASE_POOL_MAXCONN", "25")),
}

SQLALCHEMY_DATABASE_URI = (
    PGSQL["backend_code_challenge_conn"]
    if PGSQL["backend_code_challenge_conn"] != "MOCK"
    else "sqlite:///app.db"
)
