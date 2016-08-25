from .base import FunctionalTest
import time

class LoginTest(FunctionalTest):
    tu = {'id_last_name':'Иванов', 'id_first_name':'Иван Иванович','id_department':'Капстрой','id_position':'Ведущий инженер','id_phone':'33-33-33'}
    def check_record(self,rec):
        return all([self.browser.find_element_by_id(name).get_attribute('value')==self.tu[name] for name in self.tu])

    def test_change_user_attr(self):
        self.browser.get(self.server_url)
        self.browser.find_element_by_link_text('Логин').click()
        self.browser.find_element_by_id('id_login').send_keys('Test')
        self.browser.find_element_by_id('id_pass').send_keys('123\n')  
        self.browser.find_element_by_link_text('Test').click()
        self.assertEqual('Test',self.browser.find_element_by_tag_name('H1').text)
        self.browser.find_element_by_id('id_last_name').send_keys(self.tu['id_last_name'])
        self.browser.find_element_by_id('id_first_name').send_keys(self.tu['id_first_name'])
        self.browser.find_element_by_id('id_department').send_keys(self.tu['id_department'])
        self.browser.find_element_by_id('id_position').send_keys(self.tu['id_position'])
        self.browser.find_element_by_id('id_phone').send_keys(self.tu['id_phone']+'\n')
        self.browser.find_element_by_class_name('navbar-brand').click()       
        self.browser.find_element_by_link_text('Test').click()         
        self.assertTrue(self.check_record(self.tu))
        
        


