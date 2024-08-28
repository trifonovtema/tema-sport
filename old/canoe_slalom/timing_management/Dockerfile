FROM python:3.12
WORKDIR /app
COPY ./backend /app/backend
WORKDIR /app/backend/canoe_slalom/timing_management
RUN pip install -r requirements.txt
ENV PYTHONPATH="/app"
CMD ["gunicorn", "backend.canoe_slalom.timing_management.main:app", "-w", "1", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:8000"]
