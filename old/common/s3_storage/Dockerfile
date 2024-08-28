FROM python:3.12
WORKDIR /app
COPY ./backend /app/backend
WORKDIR /app/backend/common/s3_storage
RUN pip install -r requirements.txt
ENV PYTHONPATH="/app"
CMD ["gunicorn", "backend.common.s3_storage.main:app", "-w", "1", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:8000"]
