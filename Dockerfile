FROM python:3.9-slim-bullseye

WORKDIR /code

COPY ./requirements.txt /code/

RUN pip install -r requirements.txt

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

# Add option "--proxy-headers" if running behind a proxy (Nginx, ...)
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--proxy-headers"]
