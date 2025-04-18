# Importing necessary libraries
from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient
from routes import template_router, tool_router, user_router, server_router, ServerRelationship_router
import os

# Loading environment variables from the .env file into a dictionary (MONGODB_URI, DB_NAME)
config = dotenv_values(".env")

# Initializing the FastAPI app instance for defining API routes and handling requests
app = FastAPI()

# Connecting to the Mongodb database when the FastAPI app starts
@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(config["MONGODB_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]
    print("Connected to the MongoDB database!")

# Closing the Mongodb connection when the FastAPI app shuts down
@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

# Root endpoint to confirm the API is running
@app.get("/")
async def root():
    return {"message": "Welcome to the Monitoring Template Repository!"}

# Registering all the routes for the API with tags and URL prefixes
app.include_router(template_router, tags=["monitoring_templates"], prefix="/template")
app.include_router(tool_router, tags=["monitoring_tools"], prefix="/tool")
app.include_router(user_router, tags=["users"], prefix="/user")
app.include_router(server_router, tags=["servers"], prefix="/server")
app.include_router(ServerRelationship_router, tags=["links"], prefix="/link")