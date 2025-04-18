# Importing necessary libraries
import uuid
from typing import List
from pydantic import BaseModel, Field
from datetime import datetime

# Pydantic model representing a monitoring template document in the database
class MonitoringTemplate(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
    temp_name: str
    description: str
    limit: float
    unit: str
    time_window: str
    alerting_method: str
    monitoring_tools: List[str]

    # Configuration for the Pydantic model, including example data for documentation
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

# Pydantic model representing a monitoring tool document in the database
class MonitoringTool(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
    name: str
    version: str
    platform: str
    manufacturer: str
    sys_owner: str
    serv_name: str
    monitoring_templates: List[str]

    # Configuration for the Pydantic model, including example data for documentation
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

# Pydantic model representing a user document in the database
class User(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
    username: str
    email: str
    role: str
    created_at: str

    # Configuration for the Pydantic model, including example data for documentation
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

# Pydantic model representing a server document in the database
class Server(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
    hostname: str
    ip_address: str
    location: str
    owner_id: str

    # Configuration for the Pydantic model, including example data for documentation
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

# Pydantic model representing a ServerRelationship document in the database
class ServerRelationship(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
    server_id: str
    template_id: str
    tool: str
    applied_on: datetime

    # Configuration for the Pydantic model, including example data for documentation
    class Config:
        validate_by_name = True
        json_schema_extra = {
            "example": {
                "server_id": "id-123",
                "template_id": "id-456",
                "tool": "id-789",
                "applied_on": "2021-04-16 10:00:00"
            }
        }

# Pydantic model used for updating an existing monitoring template
class MonitoringTemplateUpdate(BaseModel):
    temp_name: str
    description: str
    limit: float
    unit: str
    time_window: str
    alerting_method: str
    monitoring_tools: List[str]

# Pydantic model used for updating an existing monitoring tool
class MonitoringToolUpdate(BaseModel):
    name: str
    version: str
    platform: str
    manufacturer: str
    sys_owner: str
    serv_name: str
    monitoring_templates: List[str]

# Pydantic model used for updating an existing user
class UserUpdate(BaseModel):
    username: str
    email: str
    role: str
    created_at: str

# Pydantic model used for updating an existing server
class ServerUpdate(BaseModel):
    hostname: str
    ip_address: str
    location: str
    owner_id: str

# Pydantic model used for updating an existing server-template relationship
class ServerRelationshipUpdate(BaseModel):
    server_id: str
    template_id: str
    tool: str
    applied_on: datetime