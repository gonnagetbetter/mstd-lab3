FROM python:slim-bullseye

WORKDIR /app

COPY requirementcs.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["uvicorn", "spaceship.main:app", "--host=0.0.0.0", "--port=8080"]
