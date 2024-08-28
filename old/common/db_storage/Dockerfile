FROM python:3.12
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY ./backend /app/backend
WORKDIR /app/backend/common/db_storage
ENV PYTHONPATH="/app"
CMD ["gunicorn", "backend.common.db_storage.main:app", "-w", "1", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:8000"]
