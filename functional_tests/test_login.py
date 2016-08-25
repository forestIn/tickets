from .base import FunctionalTest

class LoginTest(FunctionalTest):

    def test_login_logout(self):
        self.browser.get(self.server_url)
        self.browser.find_element_by_link_text('Логин').click()
        self.browser.find_element_by_id('id_login').send_keys('Test')
        self.browser.find_element_by_id('id_pass').send_keys('123\n')  
        self.assertEqual('Test',self.browser.find_element_by_link_text('Test').text)
        self.browser.find_element_by_link_text('Выйти').click()
        self.assertEqual('Регистрация',self.browser.find_element_by_link_text('Регистрация').text)
    

