FROM python:3.8-slim-buster

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt

COPY . /app

RUN python manage.py populate_nba_data

EXPOSE 5000

CMD ["python", "manage.py", "runserver", "--host", "0.0.0.0", "--port", "5000"]
