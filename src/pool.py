import atexit

from psycopg_pool import ConnectionPool

from config import PGSQL


backend_code_challenge_pool = ConnectionPool(
    conninfo=PGSQL["backend_code_challenge_conn"],
    min_size=PGSQL["minconn"],
    max_size=PGSQL["maxconn"],
    name="backend-code-challenge-pool",
    open=True,
)


def shutdown_pool():
    backend_code_challenge_pool.close()


atexit.register(shutdown_pool)
