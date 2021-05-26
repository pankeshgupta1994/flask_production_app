FROM python:3.6

COPY requirements.txt /usr/src/app/

RUN pip3 install -r /usr/src/app/requirements.txt
RUN pip3 install --upgrade git+https://github.com/broadinstitute/keras-resnet
COPY . /usr/src/app

WORKDIR /usr/src/app

ENV port 5000
ENV APP_ENV development
ENV cloudsight_api_key hOYp5eBuXW7CjONn3wsG6w
ENV cloudsight_api_secret Oe3vUUIOHVIiBNfZSXynbA
ENV mongoport 27017
ENV mongohost 127.0.0.1
ENV table user
ENV database Signup

EXPOSE $port
EXPOSE $mongoport

ENTRYPOINT ["python3","-u", "wsgi.py"]

