from .base import FunctionalTest

class LayoutAndStylingTest(FunctionalTest):

    def test_layout_and_styling(self):
        
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024, 768)
        #  just check line interval
        self.assertEqual('24px', self.browser.find_element_by_link_text('Логин').value_of_css_property('line-height'))
