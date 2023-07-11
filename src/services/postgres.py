import os
import psycopg

from psycopg import sql

from helpers import Formatter
from logger import LOGGER


class Postgres:
    """Class for Postgres related functions."""

    def __init__(self, pool=None):
        self.pool = pool

    def _fetch_query(self, query_file):
        with open(
            os.path.join(
                os.path.abspath(
                    os.path.join(os.path.dirname(__file__), "..", "api")
                ),
                query_file,
            ),
            "r",
            encoding="utf-8",
        ) as sql_file:
            query = sql_file.read()

        return sql.SQL(query)

    def build_query(self, **kwargs):
        try:
            if not kwargs.get("query_name"):
                raise ("Failed to find query. Must provide query_name param.")

            query = self._fetch_query(kwargs["query_name"])

            kwargs.pop("query_name")

            if kwargs:
                filters = {}

                for key, value in kwargs.items():
                    if isinstance(value, list):
                        filters[key] = sql.SQL(",").join(
                            map(sql.Literal, value)
                        )
                    elif isinstance(value, str):
                        filters[key] = sql.Identifier(value)
                    elif isinstance(value, int):
                        filters[key] = sql.Literal(value)

                formatted_query = query.format(**filters)

                return formatted_query

            return query
        except Exception as e:
            raise (f"{e}")

    def health_check(self):
        LOGGER.info("Executing query to check Postgres' health")

        if self.pool is None:
            self._open_pool()

        try:
            with self.pool.getconn() as conn:
                with conn.cursor() as cur:
                    query = "SELECT 1;"

                    cur.execute(query)

                cur.close()

            LOGGER.info("Success checking Postgres' health")
            return True

        except Exception as e:
            LOGGER.warning(e)
            return False

    def execute_query(
        self, query, should_format=False, format_camel_case=False
    ):
        LOGGER.info("Executing query")

        try:
            if self.pool is None:
                LOGGER.info(
                    "Failed to access connection pool. Will re-open pool."
                )

                self.pool.open()

            with self.pool.connection() as conn:
                LOGGER.info(query.as_string(conn))

                with conn.cursor() as cur:
                    cur.execute(query)

                    if should_format:
                        data = Formatter().format_cursor(
                            cur, format_camel_case
                        )
                    else:
                        data = int(cur.rowcount)

                cur.close()

            return data
        except psycopg.DataError as e:
            LOGGER.warning(f"Data Error: {e}")
            raise Exception(f"Data Error: {e}")
        except psycopg.OperationalError as e:
            LOGGER.warning(f"Operational Error: {e}")
            raise Exception(f"Operational Error: {e}")
        except psycopg.DatabaseError as e:
            LOGGER.warning(f"Database Error: {e}")
            raise Exception(f"Database Error: {e}")
        except Exception as e:
            LOGGER.warning(f"General DB error, {e}")
            raise Exception(f"General DB Error: {e}")
