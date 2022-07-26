FROM python:3.9

COPY ./requirements.txt /web/requirements.txt
COPY ./app /web/app

WORKDIR /web

RUN pip install -r /web/requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
