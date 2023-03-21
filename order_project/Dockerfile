FROM python:3

RUN apt-get update && apt-get install -y

WORKDIR /web
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .