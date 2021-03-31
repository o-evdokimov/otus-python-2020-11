FROM python:3.8.8-buster

WORKDIR /var/app

#COPY ../flask_demo_dev/requirements.txt requirements.txt
#RUN pip install -r requirements.txt
RUN pip install poetry
RUN poetry config virtualenvs.create false
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-interaction

COPY /razlivalka ./
RUN ls -la

EXPOSE 5000
CMD python main
