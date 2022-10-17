# frontend/Dockerfile
FROM python:3.9

ENV PIP_DISABLE_PIP_VERSION_CHECK=on
ARG CRYPTOGRAPHY_DONT_BUILD_RUST=1

RUN pip install --upgrade pip
RUN pip install poetry

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction

COPY . /app

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]
