import uuid
from typing import List
from pydantic import BaseModel, Field

class MonitoringTemplate(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
    temp_name: str
    description: str
    limit: float
    unit: str
    time_window: str
    alerting_method: str
    monitoring_tools: List[str]
    '''created_by_user_id: str
    created_at: str'''

    class Config:
        validate_by_name = True
        json_schema_extra = {
            "example": {
                "temp_name": "CPU Load",
                "description": "Monitors CPU usage over a given time period.",
                "limit": 85.0,
                "unit": "%",
                "time_window": "5min",
                "alerting_method": "Email Alert",
                "monitoring_tools": ["789e1234-a567-bcde-1234-56789abcdef0"]
            }
        }

        '''created_by_user_id": "789e1234-56789abcdef0",
        "created_at": "2021-04-01 12:00:00"'''

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
                "username": "Diya Palmgrove",
                "email": "diya.palmgrove@stud.fhgr.ch",
                "role": "Admin",
                "created_at": "2021-04-01 10:00:00"
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
    '''created_by_user_id: str
    created_at: str'''

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

