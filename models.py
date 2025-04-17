import uuid
from typing import List
from pydantic import BaseModel, Field
from datetime import datetime

class MonitoringTemplate(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
    temp_name: str
    description: str
    limit: float
    unit: str
    time_window: str
    alerting_method: str
    monitoring_tools: List[str]

    class Config:
        validate_by_name = True
        json_schema_extra = {
            "example": {
                "temp_name": "Prozess Überwachung",
                "description": "Die Laufzeit eines Prozesses wird geprüft",
                "limit": 85.0,
                "unit": "%",
                "time_window": "0min",
                "alerting_method": "Wird der Prozess nichrt mehr ausgeführt, so erfolgt ein Alarm via SMS sowie ein Mail an ServiceNow um ein Ticket zu eröffnen",
                "monitoring_tools": ["Zabbix"]
            }
        }

class MonitoringTool(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
    name: str
    version: str
    platform: str
    manufacturer: str
    sys_owner: str
    serv_name: str
    monitoring_templates: List[str]

    class Config:
        validate_by_name = True
        json_schema_extra = {
            "example": {
                "name": "Zabbix",
                "version": "6.0",
                "platform": "Linux",
                "manufacturer": "Zabbix LLC",
                "sys_owner": "IT Admin",
                "serv_name": "Monitoring-Server-1",
                "monitoring_templates": ["123e4567-e89b-12d3-a456-426614174000"]
            }
        }

class User(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
    username: str
    email: str
    role: str
    created_at: str

    class Config:
        validate_by_name = True
        json_schema_extra = {
            "example": {
                "username": "user",
                "email": "user@user.com",
                "role": "Admin",
                "created_at": "2021-04-01 10:00:00"
            }
        }

class Server(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
    hostname: str
    ip_address: str
    location: str
    owner_id: str

    class Config:
        validate_by_name = True
        json_schema_extra = {
            "example": {
                "hostname": "db01",
                "ip_address": "192.168.0.1",
                "location": "Location 1",
                "owner_id": "user-uuid"
            }
        }

class ServerRelationship(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
    server_id: str
    template_id: str
    tool_id: str
    applied_on: datetime

    class Config:
        validate_by_name = True
        json_schema_extra = {
            "example": {
                "server_id": "id-123",
                "template_id": "id-456",
                "rool_id": "id-789",
                "applied_on": "2021-04-16 10:00:00"
            }
        }

class MonitoringTemplateUpdate(BaseModel):
    temp_name: str
    description: str
    limit: float
    unit: str
    time_window: str
    alerting_method: str
    monitoring_tools: List[str]

class MonitoringToolUpdate(BaseModel):
    name: str
    version: str
    platform: str
    manufacturer: str
    sys_owner: str
    serv_name: str
    monitoring_templates: List[str]

class UserUpdate(BaseModel):
    username: str
    email: str
    role: str
    created_at: str

class ServerUpdate(BaseModel):
    hostname: str
    ip_address: str
    location: str
    owner_id: str

class ServerRelationshipUpdate(BaseModel):
    server_id: str
    template_id: str
    tool_id: str
    applied_on: datetime