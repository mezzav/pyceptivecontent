from pyceptivecontent.exceptions.user import UserNotFoundError

import pytest
import os
import vcr
import secrets
import string


class TestUser:
    # Set up default cassette options
    vcr_user = vcr.VCR(
        cassette_library_dir='tests/cassettes/user',
        serializer='json'
    )

    @vcr_user.use_cassette('user_valid.json')
    def test_get_user(self, valid_user, pytestconfig):
        id = os.getenv("USER_ID")
        username = os.getenv("USER_USERNAME")

        assert valid_user.id == id
        assert valid_user.username == username

    @vcr_user.use_cassette("user_invalid.json")
    def test_get_invalid_user(self, pyceptivecontent_session, pytestconfig):
        id = os.getenv("USER_ID") + "09QSXB"

        with pytest.raises(UserNotFoundError):
            pyceptivecontent_session.user.info(id = id)


    @vcr_user.use_cassette("user_all_users.json")
    def test_get_all_users(self, pyceptivecontent_session, pytestconfig):
        users = pyceptivecontent_session.user.all()

        assert len(users) != 0 

    @vcr_user.use_cassette("user_get_groups.json")
    def test_get_groups_from_user(self, pyceptivecontent_session, valid_user):

        groups = pyceptivecontent_session.user.groups(valid_user)

        assert isinstance(groups, list) == True
        assert len(groups) != 0

    @vcr_user.use_cassette("user_no_groups.json")
    def test_get_groups_from_empty_user(self, pyceptivecontent_session, empty_user):

        groups = pyceptivecontent_session.user.groups(empty_user)

        assert isinstance(groups, list) == True
        assert len(groups) == 0

    @vcr_user.use_cassette("user_update_profile.json")
    def test_update_profile(self, pyceptivecontent_session, empty_user):
        email = "email@example.com"

        old_email = empty_user.contactInfo.email

        empty_user.contactInfo.email = email

        assert email != old_email
        assert pyceptivecontent_session.user.updateProfile(empty_user) == True

        empty_user.contactInfo.email = old_email

        assert pyceptivecontent_session.user.updateProfile(empty_user) == True

    