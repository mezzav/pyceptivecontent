from pyceptivecontent.models.drawer import DrawerInfoModel, DrawerModel
from pyceptivecontent.exceptions.drawer import DrawerNotFoundError

import pytest
import os
import vcr

class TestDrawer:
    # Set up default cassette options
    vcr_drawer = vcr.VCR(
        cassette_library_dir='tests/cassettes/drawer',
        serializer='json'
    )


    @vcr_drawer.use_cassette("drawer_all.json")
    def test_all_drawers(self, pyceptivecontent_session):
        
        drawers = pyceptivecontent_session.drawer.all()

        assert isinstance(drawers, list)
        assert len(drawers) != 0


    @vcr_drawer.use_cassette("drawer_valid_drawer.json")
    def test_valid_drawer_info(self, pyceptivecontent_session, valid_drawer):

        drawerInfo = pyceptivecontent_session.drawer.info(drawer = valid_drawer)
    
        assert isinstance(drawerInfo, DrawerInfoModel)

    @vcr_drawer.use_cassette("drawer_invalid_drawer.json")
    def test_invalid_drawer_info(self, pyceptivecontent_session):

        invalidDrawer = DrawerModel(id = "321Z2345_072K3203749489", name = "Invalid Drawer")

        with pytest.raises(DrawerNotFoundError):
            drawerInfo = pyceptivecontent_session.drawer.info(drawer = invalidDrawer)



