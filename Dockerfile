FROM alpine:3.10

RUN apk add --no-cache python3

RUN pip3 install --upgrade pip

WORKDIR /app

COPY . /app

RUN pip --no-cache-dir install -r requirements.txt
