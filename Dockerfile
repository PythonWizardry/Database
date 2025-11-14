FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    pkg-config \
    default-libmysqlclient-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY all_requirements.txt .
RUN pip install --no-cache-dir -r all_requirements.txt

COPY . .

# Create symlink so /app/config points to actual config location
RUN ln -s /app/Lab_4-5/flask_project/app/config /app/config

EXPOSE 5000

ENV PYTHONPATH=/app 

CMD ["python", "Lab_4-5/flask_project/app/app.py"]