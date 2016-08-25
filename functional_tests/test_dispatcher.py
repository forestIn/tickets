from .base import FunctionalTest
import time

class DispatcherTest(FunctionalTest):

    def test_dispatcher_action(self):
        self.browser.get(self.server_url)
        self.browser.find_element_by_link_text('Логин').click()
        self.browser.find_element_by_id('id_login').send_keys('dispatcher')
        self.browser.find_element_by_id('id_pass').send_keys('123\n')  
        self.browser.find_element_by_link_text('Диспетчер').click()