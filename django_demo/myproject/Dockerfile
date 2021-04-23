FROM python:3.8.8-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /var/app
RUN pip install poetry
RUN poetry config virtualenvs.create false
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-interaction

COPY ./ ./
RUN ls -la

EXPOSE 8000
CMD python /var/app/manage.py runserver 0.0.0.0:8000
