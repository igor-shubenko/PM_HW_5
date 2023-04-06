# syntax=docker/dockerfile:1

FROM python:3.10.8-slim

RUN pip install --no-cache-dir --upgrade pip

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN adduser --disabled-password math_server_user
USER math_server_user

EXPOSE 8766/tcp

ENV CRUD_SERVER_LINK=$CRUD_SERVER_LINK

ENTRYPOINT ["python", "math_operations_server.py"]

