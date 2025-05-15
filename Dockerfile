# Dockerfile
FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV GOOGLE_APPLICATION_CREDENTIALS="/app/key.json"

EXPOSE 8080

CMD ["python", "main.py"]
