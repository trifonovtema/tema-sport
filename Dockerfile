FROM python:3.11-slim-bullseye
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY . /app
RUN pip install --no-cache -r /app/requirements.txt
CMD ["python", "-m", "main"]
RUN apt-get update \
    && apt-get install -y ffmpeg \
    && rm -rf /var/lib/apt/lists/*