FROM python:3.8.8-buster

WORKDIR /var/app

COPY ../flask_demo_dev/requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ../flask_demo_dev .
RUN ls -la

EXPOSE 5000
CMD python main