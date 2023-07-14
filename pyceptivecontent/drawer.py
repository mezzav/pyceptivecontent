from pyceptivecontent.base import PyceptiveContentBase
from pyceptivecontent.endpoints import API_PATH
from pyceptivecontent.models.drawer import DrawerInfoModel, DrawerModel
class Drawer(PyceptiveContentBase):
    def __init__(self, auth):
        super().__init__(auth)

    @PyceptiveContentBase._required_args(params = ["drawer"])
    def info(self, *argc, **kwargs):
        response, code, err = self._auth.request(
            method = "GET", path = API_PATH["drawer_info"].format(id = kwargs["drawer"].id)
        )

        if not response.ok:
            self.raiseException(code, err)

        data = response.json()

        return DrawerInfoModel(**data)

    
    def all(self):
        response, code, err = self._auth.request(
            method = "GET", path = API_PATH["all_drawers"]
        )

        if not response.ok:
            self.raiseException(code, err)

        data = response.json()

        drawers = []
        for drawer in data["drawers"]:
            drawers.append(DrawerModel(**drawer))

        return drawers