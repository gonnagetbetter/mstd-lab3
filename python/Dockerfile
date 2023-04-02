FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt requirements.txt

RUN apk add --no-cache musl-dev g++ gcc lapack-dev

RUN pip3 install -r requirements.txt

COPY . .

CMD ["uvicorn", "spaceship.main:app", "--host=0.0.0.0", "--port=8080"]
