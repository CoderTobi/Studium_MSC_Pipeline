import os
import asyncpg
from fastapi import FastAPI, HTTPException

app = FastAPI()

# Retrieve database URL from environment variables, with a fallback default
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://username:password@localhost:5432/mydatabase")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/db")
async def db_check():
    try:
        # Attempt to connect to the PostgreSQL database
        conn = await asyncpg.connect(DATABASE_URL)
        await conn.close()
        return {"status": "ok", "database": "connected"}
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Database connection failed: {str(e)}"
        )