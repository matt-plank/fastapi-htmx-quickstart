FROM python:3.12

WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app app
COPY templates templates

CMD ["sh", "-c", "uvicorn app.app:app --host 0.0.0.0 --port $PORT"]
