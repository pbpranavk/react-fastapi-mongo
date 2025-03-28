from typing import Optional

from pydantic import BaseModel, Field


class SimpleModel(BaseModel):
    item: str = Field(...)


def ResponseModel(data, message):
    return {"data": [data], "code": 200, "message": message}


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
