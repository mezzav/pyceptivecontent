from pydantic import BaseModel, Field

from typing import Optional

class FormBaseModel(BaseModel):
    id: str = Field(title = "id", description = "The ID of the form.")
    name: str = Field(title = "name", description = "A flag that represents if the form is active or not.")
    isDefault: bool = Field(title = "isDefault", description = "A flag to determine if it's the default form on the queue.")
    isActive: bool = Field(title = "isActive", description = "The name of the form.")