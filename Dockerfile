FROM python:3.10
ENV PYTHONBUFFERED=1
RUN mkdir /app
RUN pip install pipenv
WORKDIR /app
COPY ./edom_backend /app/
RUN pipenv lock --keep-outdated --requirements > requirements.txt
RUN pip install -r requirements.txt
