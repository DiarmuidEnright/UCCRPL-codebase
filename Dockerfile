FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    build-essential \
    libatlas-base-dev \
    libjpeg-dev \
    zlib1g-dev \
    libffi-dev \
    libssl-dev \
    libgps-dev \
    gpsd-clients \
    gpsd \
    wkhtmltopdf \
    git \
    libpython3-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN git clone https://github.com/GyroOW/rocket_code.git .

RUN pip install --upgrade pip

CMD ["python", "master.py"]
