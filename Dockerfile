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
    git \  # Added git for cloning the repository
    && rm -rf /var/lib/apt/lists/*

WORKDIR /src/src/controllers/

RUN git clone https://github.com/GyroOW/rocket_code.git .

COPY requirements.txt /src

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# EXPOSE 5000 (flask port)

CMD ["python", "gpio_controller.py"]
