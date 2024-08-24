# tema-sport

## Description
This project is designed to manage and track competitions, participants, judging, timing, and reporting for various sports, starting with canoe slalom. The architecture includes separate services for each functionality, utilizing FastAPI for backend services, Kafka for event streaming, and PostgreSQL for data storage.

## How to Run
1. Ensure Docker and Docker Compose are installed.
2. In the project root, run:
    ```
    docker-compose up --build
    ```


lsof -t -i:8000 | xargs kill -9


```shell
 python -c 'import secrets; print(secrets.token_hex())'
```