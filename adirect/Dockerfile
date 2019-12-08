FROM python:3.7.5

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt && pip install gunicorn

RUN gunicorn -b 0.0.0.0:80 run


