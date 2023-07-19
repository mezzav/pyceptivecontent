from pydantic import BaseModel, Field
from typing import Optional, Literal

class WorkflowItemModel(BaseModel):
    id: str

class WorkflowQueueBaseModel(BaseModel):
    id: str = Field(title = "id", description = "The ID of the queue")
    name: str = Field(title = "name", description = "The name of the queue")
    onHoldReasonListId: Optional[str] = Field(title = "onHoldReasonListId")
    processId: str = Field(title = "processId", description = "The ID of this queue's process")
    processName: str = Field(title = "processName", description = "The name of this queue's process")

class KeyOverrides(BaseModel):
    allowBlankField1: bool
    allowBlankField2: bool
    allowBlankField3: bool
    allowBlankField4: bool
    allowBlankField5: bool
    canModifyField1: bool
    canModifyField2: bool
    canModifyField3: bool
    canModifyField4: bool
    canModifyField5: bool

    canModifyLocation: bool
    canModifyName: bool
    canModifyProperties: bool
    canModifyType: bool
    onlyBlankFields: bool


class WorkflowQueueInfoModel(WorkflowQueueBaseModel):
    canRecallRoute: bool = Field(title = "canRecallRoute", description = "Indicates if the queue allows routed items to be recalled back to this queue")
    canRouteBack: bool = Field(title = "canRouteBack", description = "Indicates if the queue allows items to be routed back to the previous queue")
    isComplete: bool = Field(title = "isComplete", description = "Indicates if the queue is marked as a complete queue")

    keyOverrides: KeyOverrides = Field(title = "keyOverrides", description = " 	Information about the queue's key overrides.")

class RouteBaseModel(BaseModel):
    destinationQueueId: str = Field(title = "destinationQueueId", description = "The ID of the destination queue")
    destinationQueueName: str = Field(title = "destinationQueueName", description = "The name of the destination queue")

class ForwardRouteModel(RouteBaseModel):
    name: str = Field(title = "name", description = "The name of the route")
    type: Literal["MANUAL", "AUTO", "CONDITIONAL", "PARALLEL", "CONDITIONAL_PARALLEL", "PEER", "BALANCED"] = Field(title = "type", description = "The type of the route")
    defaultRoute: bool = Field(title = "defaultRoute", description = "Indicates if this is the default route")
    adHocParallelRoute: bool = Field(title = "adHocParallelRoute", description = " 	Indicates if this is an adhoc parallel route")