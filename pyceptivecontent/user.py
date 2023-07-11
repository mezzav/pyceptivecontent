from pyceptivecontent.base import PyceptiveContentBase
from pyceptivecontent.models.user import UserModel, GroupModel
from pyceptivecontent.endpoints import API_PATH


from typing import List, Dict

class User(PyceptiveContentBase):
    def __init__(self, auth):
        super().__init__(auth)


    def info(self, *argc, **kwargs) -> UserModel:
        """ 
        Retrieves information about a specific Perceptive Content user.

        :param id: user's ID
        
        :raises UserNotFoundError: A user with :param:`id` does not exist in the system. It is possible that :class:`PyceptiveContent` can not query a user
        due to privileges
        
        :return: Perceptive Content User
        :rtype: UserModel
        """

        response, code, err = self._auth.request(
            method="GET", path = API_PATH["user_info"].format(id=kwargs["id"])
        )

        if not response.ok:
            self.raiseException(code, err)

        data = response.json()

        return UserModel(
            **data,
        )

    def all(self) -> List[Dict[str, str]]:
        """
        Retrieves all user accounts from Perceptive Content

        :return: A list of dictionary values
        :rtype: List[Dict[str,str]] 
        """
        response, code, err = self._auth.request(
            method = "GET", path = API_PATH["all_users"]
        )

        if not response.ok:
            self.raiseException(code, err)

        data = response.json()

        return data["users"]
    
    def updateProfile(self, user: UserModel) -> bool:
        """
        Updates a user profile

        :param user: updated user information

        :raises InsufficientPrivilegesError
        :returns: `True` if operations was successfull, raises `Exception` otherwise
        :rtype: bool
        """
        
        response, code, err = self._auth.request(
            method = "PUT", path = API_PATH["update_user_info"].format(id = user.id), json = user.model_dump()
        )

        if not response.ok:
            self.raiseException(code, err)

        return True
    
    def groups(self, user: UserModel) -> List[GroupModel]:
        """
        Retrieves all groups a user is associated with

        :return: a List of GroupModel
        :rtype: List[GroupModel] 
        """
        response, code, err = self._auth.request(
            method = "GET", path = API_PATH["user_group_info"].format(id = user.id)
        )

        if not response.ok:
            self.raiseException(code, err)

        data = response.json()

        return [ GroupModel(**group) for group in data["groups"] ]
