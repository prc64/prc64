FROM python:3.10

RUN pip install dice

WORKDIR /app

COPY dados.py .

CMD ["python", "dados.py"]

