FROM python:3.8.8-buster

WORKDIR /var/app
RUN pip install poetry
RUN poetry config virtualenvs.create false
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-interaction

COPY /razlivalka ./
RUN ls -la

EXPOSE 5000
CMD python main
