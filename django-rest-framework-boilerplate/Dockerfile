FROM python:3.5

RUN mkdir /app
WORKDIR /app

ADD . /app

COPY /manage.py /manage.py
RUN pip install -r requirements.txt
CMD python manage.py runserver 0.0.0.0:5000