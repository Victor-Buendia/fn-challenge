FROM python:3.12.2 AS runtime_env
RUN pip install requests psycopg2 sqlalchemy pydantic
WORKDIR /app
ENV PYTHONPATH=/usr/local/app/
ENTRYPOINT ["sh","-c"]