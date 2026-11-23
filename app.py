"""Minimale API für das CI/CD-Beispiel."""

import os

import psycopg
from fastapi import FastAPI, Response

app = FastAPI()


@app.get("/")
def hello():
    return {"message": "Hello World"}


@app.get("/health")
def health(response: Response):
    url = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/postgres")
    try:
        with psycopg.connect(url, connect_timeout=2):
            pass
    except psycopg.OperationalError:
        response.status_code = 503
        return {"status": "error", "database": "nicht erreichbar"}
    return {"status": "ok", "database": "erreichbar"}
