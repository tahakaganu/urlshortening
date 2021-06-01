FROM python:latest

LABEL MAINTAINER="Daniel Santos"

ENV GROUP_ID=1000 \
    USER_ID=1000

WORKDIR /var/www/

ADD . /var/www/
RUN pip install -r requirements.txt
RUN pip install gunicorn

RUN groupadd --gid $GROUP_ID www
RUN adduser www --uid $USER_ID --gid $GROUP_ID

USER www

EXPOSE 8080

CMD [ "gunicorn", "-w", "4", "--bind", "0.0.0.0:5000", "wsgi"]