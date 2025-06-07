FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir flask pymongo python-dotenv

ENV PORT=3000
ENV HOST=0.0.0.0

CMD ["python", "app.py"]

