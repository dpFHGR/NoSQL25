from fastapi import FastAPI, Depends
from dotenv import dotenv_values
from db import get_database # Import from db.py
from routes import router as monitoring_router

config = dotenv_values(".env")

app = FastAPI()

app.include_router(monitoring_router, tags=["monitoring"], prefix="/monitoring")
