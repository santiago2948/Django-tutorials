FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Install system dependencies required for some Python packages (MySQL client, build tools)
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        default-libmysqlclient-dev \
        gcc \
        libssl-dev \
        libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

# Copy project
COPY . /app

# Use a non-root user for running the app
RUN useradd -m django && chown -R django:django /app
USER django

EXPOSE 8000

# Default command: run Gunicorn
CMD ["gunicorn", "helloworld_project.wsgi:application", "--bind", "0.0.0.0:8000"]
