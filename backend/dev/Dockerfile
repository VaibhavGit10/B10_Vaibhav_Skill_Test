FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Set environment variables for dev backend
ENV PORT=3001
ENV HOST=0.0.0.0

CMD ["python", "app.py"]
