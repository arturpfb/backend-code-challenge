FROM python:3.11.1 as python-base

ENV POETRY_VERSION=1.3.1 \
    POETRY_HOME="/opt/poetry" \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    APPLICATION_NAME="backend-code-challenge"

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

RUN apt-get update -qq && apt-get upgrade -y > /dev/null \
    && apt-get install --no-install-recommends -y curl dumb-init > /dev/null \
    && curl -sSL https://install.python-poetry.org | POETRY_HOME=$POETRY_HOME \
    python3 - --version $POETRY_VERSION \
    && addgroup --gid 1001 $APPLICATION_NAME \
    && adduser --disabled-password --disabled-login --home /app --uid 1001 \
    --gid 1001 $APPLICATION_NAME > /dev/null \
    && mkdir $PYSETUP_PATH && chown 1001 $PYSETUP_PATH

USER 1001

# ------------ END BASE ------------

# ------------ START BUILDER BASE ------------
FROM python-base as builder-base

WORKDIR $PYSETUP_PATH

COPY ./poetry.lock ./pyproject.toml ./
# ------------ END BUILDER BASE ------------

# ------------ START DEV DEPS ------------
FROM builder-base as dev-deps

RUN poetry install --no-interaction

WORKDIR /code
# ------------ END DEV DEPS ------------

# ------------ START PROD DEPS ------------
FROM builder-base as prod-deps

RUN poetry install --only main --no-interaction
# ------------ END PROD DEPS ------------


# ------------ START PRODUCTION ------------
FROM python-base as production

WORKDIR /code

COPY --chown=1001:1001 --from=prod-deps $VENV_PATH $VENV_PATH

ADD --chown=1001:1001 . /code/

EXPOSE 3000

CMD ["dumb-init", "/bin/bash", "init.sh"]
