import os

if not os.environ.get("PRODUCTION"):
    from dotenv import load_dotenv

    load_dotenv()

APP_NAME = "backend-code-challenge"

DEBUG = os.environ.get("DEBUG", False)
PORT = os.environ.get("PORT", 4000)

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
