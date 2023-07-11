from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import List
from datetime import datetime
from typing import Optional, Literal

from pyceptivecontent.models.workflow import WorkflowItemModel


class DocumentKeysModel(BaseModel):
    "Model representing document/index keys"

    model_config = ConfigDict(extra = "ignore")

    drawer: str = Field(title = "drawer", description = "drawer")
    field1: str = Field(title = "field1", description="First index key")
    field2: str = Field(title = "field2", description="Second index key")
    field3: str = Field(title = "field3", description="Third index key")
    field4: str = Field(title = "field4", description="Fourth index key")
    field5: str = Field(title = "field5", description="Fifth index key")
    type: str = Field(title = "type", description =  "Document type", alias="documentType")

class PagesModel(BaseModel):
    """Model representing a 'page' within a document."""
    model_config = ConfigDict(extra = "ignore")

    id: str = Field(title = "id", description = "Unique id of the page")
    extension: str = Field(title = "extension", description = "File type extension of the page")
    name: Optional[str] = Field(title="name", description = "Name of the page (if any)")
    pageNumber: int = Field(title="pageNumber", description = "Numerical ordering of the page")

class CustomPropertyModel(BaseModel):
    id: str = Field(title = "id", description = "Unique ID of the custom property")
    type: Literal["STRING", "NUMBER", "DATE", "FLAG", "LIST", "USER_GROUP", "USER_LIST", "COMPOSITE", "ARRAY"] = Field(title = "type", description = "Type of custom property")
    value: Optional[str] = Field(title = "id", description = "Value of the custom property")

class DocumentModel(BaseModel):
    """Pydantic model representing a Perceptive Content document."""
    id: str = Field(title="id", description = "ID of the document")
    name: str = Field(title = "name", description = "Name of the document")
    keys: DocumentKeysModel = Field(title = "keys", description = "Index values representing the document")
    pages: list[PagesModel] = Field(title = "pages", description = "List of pages within the document")
    properties: list[CustomPropertyModel] = Field(title = "properties", description = "List of custom properties associated with the document", alias="properties")
    worklowItems: list[WorkflowItemModel] = Field(title = "workflowItems", description = "List of workflowItems associated with the document", alias="workflowItems")



class DocumentSignatureModel(BaseModel):
    """Model represting a digital signature(red ribbon)"""
    id: str = Field(title = "id", description = "The digital signature's id")
    reason: str = Field(title = "reason", description = "The reason associated with the digital signature")
    status: Literal["VALID", "EXPIRED", "INVALID", "VOIDED", "VOIDED_KEY_PAIR"] = Field(title = "status", description = "status of the digital signature")
    statusTime: datetime = Field(title = "statusTime", description = "The time the status was last changed")
    validSignature: bool = Field(title = "validSignature", description = "Is the digital signature valid")
    versionId: str = Field(title = "versionId", description = "The version id of the instance this signature is for")
    versionNumber: int = Field(title = "versionNumber", description = "The version number of the instance this signature is for")
    creationUsername: str = Field(title = "creationUsername", description = "The username of the digital signature owner")
    creationTime: datetime = Field(title = "creationTime", description = "The time the instance was signed")

    @field_validator('statusTime', 'creationTime')
    def convert_to_datetime(cls, value):
        """Converts a long (unix epoch time) to a datetime object"""
        return datetime.fromtimestamp(value / 1000)