from pydantic import BaseModel, Field
from typing import Optional, List, Literal

from pyceptivecontent.models.user import IdentityInfoModel

class KeyValuePairModel(BaseModel):
    key: str = Field(title = "key", description = "The key")
    value: str = Field(title = "value", description = "The value")

class DocumentTypeModel(BaseModel):
    id: str = Field(title="id", description="")
    name: str = Field(title="name", description="")
    description: Optional[str] = Field(title="description", default = None, description="")

class CustomPropertyUserInfoModel(IdentityInfoModel):
    username: Optional[str] = Field(title = "username", description = "The username of the user")


class ChildPropertyModel(BaseModel):
    id: str = Field(title = "id", description = "The ID of the child property")
    isRequired: bool = Field(title = "isRequired", description = "Indicates if this child property is required")

class DocumentTypePropertyModel(BaseModel):
    required: bool = Field(title = "requried", description = "")
    children: Optional[List[ChildPropertyModel]] = Field(title = "children", description = "Children's list for composite and array type, it only has property id and isRequired field")
    defaultValue: Optional[str] = Field(title = "defaultValue", description = "The default vlaue for this property")
    formats: Optional[List[KeyValuePairModel]] = Field(title = "formats", description = "How to display this property")
    id: str = Field(title = "id", description = "The ID of the property")
    listValueCandidates: Optional[List[str]] = Field(title = "listValueCandidates")
    name: str = Field(title = "name", description = "The name of property")
    type: Literal["STRING", "NUMBER", "DATE", "FLAG", "LIST", "USER_GROUP", "USER_LIST", "COMPOSITE", "ARRAY"] = Field(title = "type", description = "Enum property type")
    userGroupId: Optional[str] = Field(title = "userGroupId", description = "User group id for user group type")
    userGroupName: Optional[str] = Field(title = "userGroupName", description = "User group name for user group type")
    userList: Optional[CustomPropertyUserInfoModel] = Field(title = "userList", description = "User list for user types")

class DocumentTypeInfoModel(DocumentTypeModel):
    formId: Optional[str] = Field(title = "formId", description = "The unique form id for an associated form")
    properties: List[DocumentTypePropertyModel] = Field(title = "properties", description = "The custom properties associated with the document type")

class DocumentTypeListModel(BaseModel):
    id: str = Field(title="id", description="The unique id of the document type list")
    name: str = Field(title="name", description="The name of the document type list")
    description: Optional[str] = Field(title="description", description="A description of the document type list")

class DocumentTypeListInfoModel(DocumentTypeListModel):
    documentTypes: Optional[List[DocumentTypeModel]] = Field(title="documentTypes", description="The document types in the list")
