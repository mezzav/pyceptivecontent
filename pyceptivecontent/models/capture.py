from pydantic import BaseModel, Field

from typing import Literal, Optional, List

from datetime import datetime

class CaptureProfileBaseModel(BaseModel):
    id: str = Field(title = "id", description = "The unique ID of the capture Profile")
    name: str = Field(title = "name", description = "The name of the capture profile as it is in our ImageNow system")
    description: str = Field(title = "description", description = "The name of the capture profile as it is in our ImageNow system")

    categoryType: Literal["ALL", "DOCUMENT", "RECORD"]
    sourceType: Literal["FAX_AGENT", "CONNECTOR_SAP", "IMPORT_AGENT", "INTERACT_OUTLOOK", "EXTERNAL", "MOBILE", "EXTERNAL_SCANNER"]
    type: Literal["AGENT", "INTERACT", "EXTERNAL", "MOBILE", "EXTERNAL_USER"]

class CaptureProfileInfoModel(CaptureProfileBaseModel):
    addToVersionControl: bool = Field(title = "addToVersionControl", description = "This indicates whether documents are added to version control when using this capture profile")
    applicationPlanId: str = Field(title = "applicationPlanId", description = " 	The ID of application plan associated with the capture profile")
    sourceProfileId: Optional[str] = Field(title  = "sourceProfileId", description = "The ID of the capture source profile associated with the capture profile")
    submitToContent: bool = Field(title = "submitToContent", description = "This indicates whether documents are submitted to Content Server when using this capture profile")
    wfQueueId: Optional[str] = Field(title = "wfQueueId", description = "This is the ID of the workflow queue in which ImageNow Server places the documents when using this capture profile")

class PropertyValueModel(BaseModel):
    id: str
    value: str

class FolderContextModel(BaseModel):
    folderTypeName: str
    name: str
    propertyValues: List[PropertyValueModel]

class ShortcutContextModel(BaseModel):
    drawerName: str
    folderContexts: List[FolderContextModel]
    shortcutName: str

class DocumentContextModel(BaseModel):
    documentName: str
    documentType: str
    field1: str
    field2: str
    field3: str
    field4: str
    field5: str
    propertyvalues: Optional[List[PropertyValueModel]] = Field(default = None)

class CaptureGroupContextModel(BaseModel):
    drawerName: str
    documentContext: DocumentContextModel
    folderContexts: List[FolderContextModel]
    shortcutContexts: List[ShortcutContextModel]
    parentFolderId: Optional[str] = Field(default = None)

class CaptureGroupInfoModel(BaseModel):
    id: str
    context: CaptureGroupContextModel

class CaptureGroupPageEmailMetadataModel(BaseModel):
    bccAddresses: Optional[List[str]]
    ccAddresses: Optional[List[str]]
    fromAddress: str
    receivedTime: Optional[datetime]
    replyToAddresses: Optional[List[str]]
    sentTime: Optional[datetime]
    subject: Optional[str]
    toAddresses: Optional[List[str]]
    

class PageMetaDataModel(BaseModel):
    fileType: str
    scanTime: datetime
    scanUserId: str
    scanUserName: str
    sourcePageNumber: int
    sourceType: Literal[
        "NONE",
        "BATCH_SCAN",
        "BATCH_IMPORT",
        "BATCH_INPRINT",
        "SINGLE_SCAN",
        "SINGLE_IMPORT",
        "SINGLE_INPRINT",
        "PACKAGE",
        "VIEWER_ADD_SCAN",
        "VIEWER_ADD_IMPORT",
        "COPY_PAGE",
        "FAX_AGENT",
        "IMP_AGENT",
        "MSG_AGENT",
        "MAIL_AGENT",
        "EOB_AGENT",
        "ISIR_AGENT",
        "ISCRIPT",
        "EH_AGENT",
        "REDACTION"
    ]
    workingName: str


class CaptureGroupPageInfoModel(BaseModel):
    emailMetadata: Optional[CaptureGroupPageEmailMetadataModel] = Field(default = None)
    emailMetadataId: Optional[str] = Field(default = None)
    pageContext: CaptureGroupContextModel
    pageMetaData: Optional[PageMetaDataModel] = Field(default = None)

class CaptureGroupPageModel(BaseModel):
    id: str = Field(alias = "documentId")
    emailMetadataId: Optional[str]
    logobId: str
    pageNumber: int
    shortcutIds: List[str]