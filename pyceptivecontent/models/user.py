from pydantic import BaseModel, Field, ConfigDict

from typing import Literal, Optional, Dict, List

class ContactInfoModel(BaseModel):
    email: Optional[str] = Field(title = "email", description = "The email address for the user")
    fax: Optional[str] = Field(title = "fax", description = "The fax number of the user")
    location: Optional[str] = Field(title = "location", description = "The location of the user")
    mobile: Optional[str] = Field(title = "mobile", description = "The mobile number of the user")
    pager: Optional[str] = Field(title = "pager", description = "The pager number of the user")
    phone: Optional[str] = Field(title = "phone", description = "The phone number of the user")

class SystemInfoModel(BaseModel):
    externalID: Optional[str] = Field(title = "externalID", description = "The external id of the user")
    org: Optional[str] = Field(title = "org", description = "The organization of the user")
    orgUnit: Optional[str] = Field(title = "orgUnit", description = "The organization unit of the user")

class IndentityInfo(BaseModel):
    firstName: Optional[str] = Field(title = "firstName", description = "The first name of the user")
    lastName: Optional[str] = Field(title = "lastName", description = "The last name of the user")
    prefix: Optional[str] = Field(title = "prefix", description = "The prefix of the user")
    suffix: Optional[str] = Field(title = "suffix", description = "The suffix of the user")
    title: Optional[str] = Field(title = "title", description = "The title of the user")

class UserModel(BaseModel):
    model_config = ConfigDict(validate_assignment=True)  

    category: Literal["REGULAR", "SYSTEM", "POOLED", "AUTO_UPDATE"] = Field(title = "category", description ="The category of the user", frozen = True)
    id: str = Field(title = "id", description = "The id of the user", frozen = True)
    isActive: bool = Field(title = "isActive", description = "Whether the user is currently active", frozen = True)
    username: str = Field(title = "username", description = "The username of the user", alias = "name", frozen = True)

    contactInfo: Optional[ContactInfoModel]
    externalSystemInfo: Optional[SystemInfoModel]
    identityInfo: Optional[IndentityInfo]


class GroupModel(BaseModel):
    model_config = ConfigDict(validate_assignment=True)  

    category: Literal["SYSTEM", "USER_DEFINED"] = Field(title = "category", description = "The category type of the user group", frozen = True)
    departmentId: str = Field(title = "departmentId", description = "The ID of the user group's department", frozen = True)
    description: str = Field(title = "description", description = "The description of the user group")
    isGloballyVisible: bool = Field(title = "isGloballyVisible", description = "A flag that represents whether the user group displays in a cross department context.", frozen = True)
    name: str = Field(title = "name", description = "The name of the user group")

class UserGroupModel(GroupModel):
    users: List[Dict[str, str]] = Field(title = "users") 
