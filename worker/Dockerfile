FROM python:3.9

WORKDIR /worker

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["celery", "-A", "worker", "worker", "--loglevel=info"]

