from pydantic import BaseModel, Field

from pyceptivecontent.models.document import DocumentKeysModel

from typing import Optional, List

class DrawerModel(BaseModel):
    id: str = Field(title = "id", description = "The unique ID of the drawer")
    name: str = Field(title = "name", description = "The name of the drawer")


class DrawerFolderModel(BaseModel):
    id: str = Field(title = "id", description = "The unique id of the folder or shortcut")
    name: str = Field(title = "name", description = "The name of the folder")
    targetId: Optional[str] = Field(title = "targetId", description = "If a shortcut, the unique id of the target folder")
    typeId: str = Field(title = "typeId", description = "The type id of the folder")

class DrawerDocumentModel(BaseModel):
    id: str = Field(title = "id", description = "The document's id")
    keys: DocumentKeysModel = Field(title = "keys", description = "The document's set of keys")
    name: str = Field(title = "name", description = "The document's name")
    targetId: Optional[str] = Field(title = "targetId", description = "If a shortcut, the unique id of the target document")

class DrawerInfoModel(DrawerModel):
    containedFolders: Optional[List[DrawerFolderModel]] = Field(title = "containedFolders", description = "The documents contained within this drawer. Does not include documents in contained folders")
    containedDocuments: Optional[List[DrawerDocumentModel]] = Field( title = "containedDocuments", description = "The folders contained within this drawer")