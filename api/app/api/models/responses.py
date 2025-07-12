from time import time
from typing import Optional

from pydantic import BaseModel, Field


def get_current_timestamp():
    return int(time())


class BaseResponse(BaseModel):
    message: Optional[str]
    timestamp: int = Field(default_factory=get_current_timestamp, example=get_current_timestamp())


class Report(BaseModel):
    sensorId: int = Field(default=None)
    measure: int = Field(...)

    class Config:
        json_schema_extra = {
            "example": {
                "sensorId": "1",
                "measure": "345"
            }
        }