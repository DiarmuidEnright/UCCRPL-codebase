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
    && rm -rf /var/lib/apt/lists/*

WORKDIR /src/src/controllers/

COPY . /src/src/controllers/gpio_controller.py

COPY requirements.txt /src/src/controllers/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


# EXPOSE 5000 (flask port)

CMD ["python", "gpio_controller"] # sample tesr