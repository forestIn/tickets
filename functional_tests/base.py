from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
import sys

from users.models import CustomUser


class FunctionalTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]                
                return
        super().setUpClass()
        cls.server_url = cls.live_server_url
        u=CustomUser(username='Test', is_active=True)
        u.set_password('123')
        u.save()

        disp=CustomUser(username='dispatcher', is_active=True, type_user='DP')
        disp.set_password('123')
        disp.save()        



    def setUp(self):        
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()


