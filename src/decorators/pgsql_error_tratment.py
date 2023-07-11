from psycopg import DataError, DatabaseError, OperationalError

from logger import LOGGER


def default_pgsql_err_treatment(func):
    def wrap(*args, **kwargs):
        try:
            LOGGER.info("Executing query")
            return func(*args, **kwargs)
        except DataError as e:
            LOGGER.warning(f"Data Error: {e}")
            raise
        except OperationalError as e:
            LOGGER.warning(f"Operational Error: {e}")
            raise
        except DatabaseError as e:
            LOGGER.warning(f"Database Error: {e}")
            raise
        except Exception as e:
            LOGGER.warning(f"General DB error, {e}")
            raise

    return wrap
