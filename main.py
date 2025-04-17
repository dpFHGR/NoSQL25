from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient
from routes import template_router, tool_router, user_router, server_router, ServerRelationship_router
import os

config = dotenv_values(".env")

app = FastAPI()

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(config["MONGODB_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]
    print("Connected to the MongoDB database!")

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

@app.get("/")
async def root():
    return {"message": "Welcome to the Monitoring Template Repository!"}

app.include_router(template_router, tags=["monitoring_templates"], prefix="/template")
app.include_router(tool_router, tags=["monitoring_tools"], prefix="/tool")
app.include_router(user_router, tags=["users"], prefix="/user")
app.include_router(server_router, tags=["servers"], prefix="/server")
app.include_router(ServerRelationship_router, tags=["links"], prefix="/link")