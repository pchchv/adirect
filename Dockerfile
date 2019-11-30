FROM python:3.7
ADD . /aDirect
WORKDIR /aDirect
RUN chmod ugo+x conf.sh
RUN /bin/bash -c "source conf.sh"
RUN pip install flask gunicorn pymorphy2 requests
EXPOSE 8000
CMD ["gunicorn", "-b", "0.0.0.0:80", "aDirect"]
