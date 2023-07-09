from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import List
from datetime import datetime

from pyceptivecontent.models.workflow import WorkflowItemModel

class DocumentKeysModel(BaseModel):
    model_config = ConfigDict(extra = "ignore")

    drawer: str
    field1: str
    field2: str
    field3: str
    field4: str
    field5: str
    type: str = Field(alias="documentType")

class PagesModel(BaseModel):
    model_config = ConfigDict(extra = "ignore")

    id: str
    extension: str
    name: str = Field(default = None)
    pageNumber: int

class CustomPropertyModel(BaseModel):
    id: str
    type: str
    value: str

class DocumentModel(BaseModel):
    id: str
    name: str
    keys: DocumentKeysModel
    pages: list[PagesModel]
    properties: list[CustomPropertyModel] = Field(default=None, alias="properties")
    worklowItems: list[WorkflowItemModel] = Field(default=None, alias="workflowItems")



class DocumentSignatureModel(BaseModel):
    id: str
    reason: str
    status: str
    statusTime: int
    validSignature: bool
    versionId: str
    versionNumber: int
    creationUsername: str
    creationTime: int 

    @field_validator('statusTime', 'creationTime')
    def convert_to_datetime(cls, value):
        return datetime.fromtimestamp(value / 1000)