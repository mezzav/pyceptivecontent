from  pyceptivecontent.base import PyceptiveContentBase
from pyceptivecontent.endpoints import API_PATH

from pyceptivecontent.models.workflow import WorkflowQueueBaseModel, RouteBaseModel, ForwardRouteModel
from pyceptivecontent.models.forms import FormBaseModel


from typing import List

class WorkflowQueue(PyceptiveContentBase):
    def __init__(self, auth):
        super().__init__(auth)

    def all(self) -> List[WorkflowQueueBaseModel]:
        response, code, err = self._auth.request(
            method = "GET", path = API_PATH["workflow_queue_all"]
        )

        if not response.ok:
            self.raiseException(code, err)

        data = response.json()

        wfQueues = []
        for queue in data["workflowQueues"]:
            wfQueues.append(WorkflowQueueBaseModel(**queue))

        return wfQueues

    @PyceptiveContentBase._required_any_args(params = ["id", "model"])
    def info(self, *argc, **kwargs):
        id = None

        if isinstance(id, str):
            id = id
        elif isinstance(id, WorkflowQueueBaseModel): 
            id = kwargs["model"].id
        else:
            raise TypeError(kwargs.keys() + " is not a supported parameter")
        
        response, code, err = self._auth.request(
            method = "GET", path = API_PATH["workflow_queue_info"].format(id = id)
        )

        if not response.ok:
            self.raiseException(code, err)

        data = response.json()

        return WorkflowQueueBaseModel(**data)
    
    def forms(self, queue: WorkflowQueueBaseModel) -> List[FormBaseModel]:
        response, code, err = self._auth.request(
            method = "GET", path = API_PATH["workflow_queue_forms"].format(id = queue.id)
        )

        if not response.ok:
            self.raiseException(code, err)

        data = response.json()

        forms = []
        for form in data['forms']:
            forms.append(FormBaseModel(**form))

        return forms
    
    def allRoutes(self, queue: WorkflowQueueBaseModel) -> List[RouteBaseModel]:
        response, code, err = self._auth.request(
            method = "GET", path = API_PATH["workflow_queue_all_routes"].format(id = queue.id)
        )

        if not response.ok:
            self.raiseException(code, err)

        data = response.json()

        routes = []
        for route in data['routes']:
            routes.append(RouteBaseModel(**route))

        return routes
        
    def forwardRoutes(self, queue: WorkflowQueueBaseModel) -> List[ForwardRouteModel]:
        response, code, err = self._auth.request(
            method = "GET", path = API_PATH["workflow_queue_forward_route"].format(id = queue.id)
        )

        if not response.ok:
            self.raiseException(code, err)

        data = response.json()

        forwardRoutes = []
        for route in data['forwardRoutes']:
            forwardRoutes.append(ForwardRouteModel(**route))

        return forwardRoutes
    
        
