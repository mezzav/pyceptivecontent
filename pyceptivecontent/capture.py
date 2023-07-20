from pyceptivecontent.base import PyceptiveContentBase
from pyceptivecontent.models.capture import CaptureProfileBaseModel, CaptureProfileInfoModel, CaptureGroupInfoModel, CaptureGroupPageInfoModel, CaptureGroupPageModel

from pyceptivecontent.exceptions.misc import FileDoesNotExistError

from pyceptivecontent.endpoints import API_PATH

from requests_toolbelt.multipart import encoder
from pathlib import Path
from typing import List, Dict
import copy

import json

class CaptureProfile(PyceptiveContentBase):

    def __init__(self, auth):
        super().__init__(auth)

    def all(self):
        response, code, err = self._auth.request(
            method = "GET", path = API_PATH["capture_profile_all"]
        )

        if not response.ok:
            self.raiseException(code, err)

        data = response.json()

        captureProfiles = []
        for profile in data["captureProfiles"]:
            captureProfiles.append(CaptureProfileBaseModel(**profile))

        return captureProfiles

    #@PyceptiveContentBase._required_any_args(params = ["id", "model"])
    def info(self, *argc, **kwargs):
        id = None

        if kwargs.get('id'):
            id = kwargs.get('id')
        elif kwargs.get('model'):
            id = kwargs.get('model').id
        else:
            raise TypeError(','.join(list(kwargs.keys())) + " is not a supported parameter.")
        
        response, code, err = self._auth.request(
            method = "GET", path = API_PATH["capture_profile_info"].format(id = id)
        )

        if not response.ok:
            self.raiseException(code, err)

        data = response.json()

        return CaptureProfileInfoModel(**data)

class CaptureGroup(PyceptiveContentBase):

    def __init__(self, auth):
        super().__init__(auth)

    def info(self, *argc, **kwargs) -> None:
        pass

    def create(self, captureProfile: CaptureProfileInfoModel, keyValuePairs: List[Dict[str, str]]):
        payload = {
            "captureProfileId": captureProfile.id,
            "sourceMetadataPairs": keyValuePairs
        }

        response, code, err = self._auth.request(
            method = "POST", path = API_PATH["capture_group_create"], json = payload
        )

        if not response.ok:
            self.raiseException(code, err)

        data = response.json()

        return CaptureGroupInfoModel(**data)

    def add(self, page: str, group: CaptureGroupInfoModel):
        
        filePath = Path(page)
        
        if not filePath.exists():
            raise FileDoesNotExistError()

        payload = CaptureGroupPageInfoModel(pageContext = group.context)
    
        multipart_fields = {
            "captureGroupPageInfo": ('captureGroupPageInfo', json.dumps(payload.model_dump()).encode('utf-8'), 'application/json'),
            'pageData': ('pageData', open(filePath, 'rb'), 'application/json')
        }

        multipart_data = encoder.MultipartEncoder(fields = multipart_fields)

        auth = copy.deepcopy(self._auth)

        auth.updateHeaders('X-IntegrationServer-File-Size', str(filePath.stat().st_size))
        auth.updateHeaders('Content-Type', multipart_data.content_type)

        response, code, err = auth.request(
            method = "POST", path = API_PATH["capture_group_add"].format(id = group.id), data = multipart_data
        )

        if not response.ok:
            self.raiseException(code, err)

        data = response.json()

        return CaptureGroupPageModel(**data)

    def close(self, captureProfile: CaptureProfileInfoModel, group: CaptureGroupInfoModel):
        params = {
            "captureProfileId": captureProfile.id
        }

        response, code ,err = self._auth.request(
            method = "PUT", path = API_PATH["capture_group_close"].format(id = group.id), params = params
        )

        if not response.ok:
            self.raiseException(code, err)

class Capture:
    def __init__(self, auth):
        self.__profile = CaptureProfile(auth)
        self.__group = CaptureGroup(auth)
    
    @property
    def profile(self) -> CaptureProfile:
        return self.__profile
    
    @property
    def group(self) -> CaptureGroup:
        return self.__group