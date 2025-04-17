from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List
from models import (MonitoringTemplate, MonitoringTemplateUpdate, MonitoringTool, MonitoringToolUpdate, User, UserUpdate, Server, ServerUpdate, ServerRelationship, ServerRelationshipUpdate)

template_router = APIRouter()
tool_router = APIRouter()
user_router = APIRouter()
server_router = APIRouter()
ServerRelationship_router = APIRouter()

# MonitoringTemplate Routes
@template_router.post("/", response_description="Create a new monitoring template", status_code=status.HTTP_201_CREATED, response_model=MonitoringTemplate)
def create_monitoring_template(request: Request, template: MonitoringTemplate = Body(...)):
    template = jsonable_encoder(template)
    new_template = request.app.database["monitoring_templates"].insert_one(template)
    created_template = request.app.database["monitoring_templates"].find_one({"_id": new_template.inserted_id})
    return created_template

@template_router.get("/", response_description="List all monitoring templates", response_model=List[MonitoringTemplate])
def list_monitoring_templates(request: Request):
    templates = list(request.app.database["monitoring_templates"].find(limit=100))
    return templates

@template_router.get("/{id}", response_description="Get a single monitoring template by id", response_model=MonitoringTemplate)
def find_monitoring_template(id: str, request: Request):
    if (template := request.app.database["monitoring_templates"].find_one({"_id": id})) is not None:
        return template
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Monitoring template with ID {id} not found")

@template_router.put("/{id}", response_description="Update a monitoring template", response_model=MonitoringTemplate)
def update_template(id: str, request: Request, template: MonitoringTemplateUpdate = Body(...)):
    template_data = {k: v for k, v in template.dict().items() if v is not None}
    if len(template_data) >= 1:
        update_result = request.app.database["monitoring_templates"].update_one({"_id": id}, {"$set": template_data})
        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Monitoring template with ID {id} not found")

    if (existing_template := request.app.database["monitoring_templates"].find_one({"_id": id})) is not None:
        return existing_template

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Monitoring template with ID {id} not found")

@template_router.delete("/{id}", response_description="Delete a monitoring template")
def delete_monitoring_template(id: str, request: Request, response: Response):
    delete_result = request.app.database["monitoring_templates"].delete_one({"_id": id})
    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Monitoring template with ID {id} not found")


# MonitoringTool Routes
@tool_router.post("/", response_description="Create a new monitoring tool", status_code=status.HTTP_201_CREATED, response_model=MonitoringTool)
def create_monitoring_tool(request: Request, tool: MonitoringTool = Body(...)):
    tool = jsonable_encoder(tool)
    new_tool = request.app.database["monitoring_tools"].insert_one(tool)
    created_tool = request.app.database["monitoring_tools"].find_one({"_id": new_tool.inserted_id})
    return created_tool

@tool_router.get("/", response_description="List all monitoring tools", response_model=List[MonitoringTool])
def list_monitoring_tools(request: Request):
    tools = list(request.app.database["monitoring_tools"].find(limit=100))
    return tools

@tool_router.get("/{id}", response_description="Get a single monitoring tool by id", response_model=MonitoringTool)
def find_monitoring_tool(id: str, request: Request):
    if (tool := request.app.database["monitoring_tools"].find_one({"_id": id})) is not None:
        return tool
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Monitoring tool with ID {id} not found")

@tool_router.put("/{id}", response_description="Update a monitoring tool", response_model=MonitoringTool)
def update_monitoring_tool(id: str, request: Request, tool: MonitoringToolUpdate = Body(...)):
    tool_data = {k: v for k, v in tool.dict().items() if v is not None}
    if len(tool_data) >= 1:
        update_result = request.app.database["monitoring_tools"].update_one({"_id": id}, {"$set": tool_data})
        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Monitoring tool with ID {id} not found")

    if (existing_tool := request.app.database["monitoring_tools"].find_one({"_id": id})) is not None:
        return existing_tool

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Monitoring tool with ID {id} not found")

@tool_router.delete("/{id}", response_description="Delete a monitoring tool")
def delete_monitoring_tool(id: str, request: Request, response: Response):
    delete_result = request.app.database["monitoring_tools"].delete_one({"_id": id})
    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Monitoring tool with ID {id} not found")


# User Routes
@user_router.post("/", response_description="Create a new user", status_code=status.HTTP_201_CREATED, response_model=User)
def create_user(request: Request, user: User = Body(...)):
    user = jsonable_encoder(user)
    new_user = request.app.database["users"].insert_one(user)
    created_user = request.app.database["users"].find_one({"_id": new_user.inserted_id})
    return created_user

@user_router.get("/", response_description="List all users", response_model=List[User])
def list_users(request: Request):
    user = list(request.app.database["users"].find(limit=100))
    return user

@user_router.get("/{id}", response_description="Get a single user", response_model=User)
def find_user(id: str, request: Request):
    if (user := request.app.database["users"].find_one({"_id": id})) is not None:
        return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User {id} not found")

@user_router.put("/{id}", response_description="Update a user", response_model=User)
def update_user(id: str, request: Request, user: UserUpdate = Body(...)):
    user_data = {k: v for k, v in user.dict().items() if v is not None}
    if len(user_data) >= 1:
        update_result = request.app.database["users"].update_one({"_id": id}, {"$set": user_data})
        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User {id} not found")

    if (existing_user := request.app.database["users"].find_one({"_id": id})) is not None:
        return existing_user

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User {id} not found")

@user_router.delete("/{id}", response_description="Delete a user")
def delete_user(id: str, request: Request, response: Response):
    delete_result = request.app.database["users"].delete_one({"_id": id})
    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User {id} not found")


# Server Routes
@server_router.post("/", response_description="Create a new server", response_model=Server)
def create_server(request: Request, server: Server = Body(...)):
    server = jsonable_encoder(server)
    new_server = request.app.database["servers"].insert_one(server)
    return request.app.database["servers"].find_one({"_id": new_server.inserted_id})

@server_router.get("/", response_description="List all servers", response_model=Server)
def list_servers(request: Request):
    server = list(request.app.database["servers"].find(limit=100))
    return server

@server_router.get("/{id}", response_description="Get a single server or list all", response_model=Server)
def find_server(id: str, request: Request):
    return list(request.app.database["servers"].find({"_id": id}, limit=100))

@ServerRelationship_router.post("/", response_description="Link template to server", response_model=ServerRelationship)
def link_template_to_server(id: str, request: Request, link: ServerRelationship = Body(...)):
    link = jsonable_encoder(link)
    new_link = request.app.database["links"].find_one({"_id": id}, link)
    return request.app.database["links"].find_one({"_id": new_link["_id"]})

@ServerRelationship_router.get("/", response_description="Get all links", response_model=List[ServerRelationship])
def list_links(request: Request):
    return list(request.app.database["links"].find(limit=100))