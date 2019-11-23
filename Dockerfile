FROM python:3.6-alpine

RUN adduser -D adirect

WORKDIR /home/jack/aDirect

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN adirectenv/bin/pip install -r requirements.txt
RUN adirectenv/bin/pip install gunicorn

COPY app app
COPY migrations migrations
COPY adirect.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP microblog.py

RUN chown -R microblog:microblog ./
USER microblog

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
