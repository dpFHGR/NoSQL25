import uuid
from typing import Optional
from pydantic import BaseModel, Field

class MonitoringTemplate(BaseModel):
    T_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    Temp_name: str
    Description: str
    Limit: float
    Unit: str
    Time_window: Optional[int]
    Alert_method: str

    class Config:
        validate_by_name = True
        json_schema_extra = {
            "example": {
                "T_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "Temp_name": "CPU Utilization",
                "Description": "Check the CPU utilization percentage.",
                "Limit": 80,
                "Unit": "%",
                "Time_window": 15,
                "Alert_method": "Warning email sent"
            }
        }

class MonitoringTemplateUpdate(BaseModel):
    Temp_name: Optional[str]
    Description: Optional[str]
    Limit: Optional[float]
    Unit: Optional[str]
    Time_window: Optional[int]
    Alert_method: Optional[str]

    class Config:
        json_schema_extra = {
            "example": {
                "Limit": 90,
                "Alert_method": "Alarm via SMS and email to ServiceNow"
            }
        }




