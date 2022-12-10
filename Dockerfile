FROM python:3.9

LABEL maintainer="JamariusTaylor"

WORKDIR /main

COPY requirements.txt /main/requirements.txt

RUN mkdir app

WORKDIR /app

COPY ./app /app

RUN pip install --no-cache-dir --upgrade -r /main/requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]