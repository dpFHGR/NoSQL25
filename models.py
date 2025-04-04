import uuid
from typing import Optional, List
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

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "123e4567-e89b-12d3-a456-426614174000",
                "temp_name": "CPU Load",
                "description": "Monitors CPU usage over a given time period.",
                "limit": 85.0,
                "unit": "%",
                "time_window": "5min",
                "alerting_method": "Email Alert",
                "monitoring_tools": ["789e1234-a567-bcde-1234-56789abcdef0"]
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
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "789e1234-a567-bcde-1234-56789abcdef0",
                "name": "Zabbix",
                "version": "6.0",
                "platform": "Linux",
                "manufacturer": "Zabbix LLC",
                "sys_owner": "IT Admin",
                "serv_name": "Monitoring-Server-1",
                "monitoring_templates": ["123e4567-e89b-12d3-a456-426614174000"]
            }
        }

class MonitoringTemplateUpdate(BaseModel):
    temp_name: Optional[str]
    description: Optional[str]
    limit: Optional[float]
    unit: Optional[str]
    time_window: Optional[str]
    alerting_method: Optional[str]
    monitoring_tools: Optional[List[str]]

class MonitoringToolUpdate(BaseModel):
    name: Optional[str]
    version: Optional[str]
    platform: Optional[str]
    manufacturer: Optional[str]
    sys_owner: Optional[str]
    serv_name: Optional[str]
    monitoring_templates: Optional[List[str]]
