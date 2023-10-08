FROM python:3.11.5

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip -r requirements.txt

ENV FLASK_APP=run.py
ENV FLASK_ENV=production

ENTRYPOINT ["sh", "./entrypoint.sh"]

