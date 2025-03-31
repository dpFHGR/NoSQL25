from fastapi import APIRouter, Body, Request, Response, HTTPException, status, Depends
from fastapi.encoders import jsonable_encoder
from typing import List
from models import MonitoringTemplate, MonitoringTemplateUpdate
from db import get_database # Import from db.py

router = APIRouter()

@router.post("/", response_description="Create a new monitoring template", status_code=status.HTTP_201_CREATED, response_model=MonitoringTemplate)
def create_template(request: Request, template: MonitoringTemplate = Body(...)):
    template = jsonable_encoder(template)
    new_template = request.app.database["monitoring_templates"].insert_one(template)
    created_template = request.app.database["monitoring_templates"].find_one({"_id": new_template.inserted_id})
    return created_template

@router.get("/", response_description="List all monitoring templates", response_model=List[MonitoringTemplate])
def list_templates(db=Depends(get_database)):
    templates = list(db["monitoring_templates"].find(limit=100))
    return templates

@router.get("/{id}", response_description="Get a single monitoring template by id", response_model=MonitoringTemplate)
def find_template(id: str, request: Request):
    if (template := request.app.database["monitoring_templates"].find_one({"T_id": id})) is not None:
        return template
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Template with ID {id} not found")

@router.put("/{id}", response_description="Update a monitoring template", response_model=MonitoringTemplate)
def update_template(id: str, request: Request, template: MonitoringTemplateUpdate = Body(...)):
    template = {k: v for k, v in template.dict().items() if v is not None}
    if len(template) >= 1:
        update_result = request.app.database["monitoring_templates"].update_one({"T_id": id}, {"$set": template})
        if update_result.matched_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Template with ID {id} not found")

    if (existing_template := request.app.database["monitoring_templates"].find_one({"T_id": id})) is not None:
        return existing_template

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Template with ID {id} not found")

@router.delete("/{id}", response_description="Delete a monitoring template")
def delete_template(id: str, request: Request, response: Response):
    delete_result = request.app.database["monitoring_templates"].delete_one({"T_id": id})
    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Template with ID {id} not found")
