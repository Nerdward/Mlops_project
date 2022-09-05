FROM python:3.8.10-slim

RUN pip install -U pip
RUN pip install pipenv

WORKDIR /code

COPY [ "Pipfile", "Pipfile.lock",  "./"]
COPY [ "model", "./model"]

COPY [ "./app",  "./app"]

RUN pipenv install --system --deploy
ENV PYTHONPATH "${PYTHONPATH}:/code/app"

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]