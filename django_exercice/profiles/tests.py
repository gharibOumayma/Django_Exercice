
from django import test
from selenium.webdriver.firefox import webdriver
from selenium.webdriver.common.keys import Keys
import time


class BasicTestWithSelenium(test.LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.selenium = webdriver.WebDriver()
        super(BasicTestWithSelenium, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(BasicTestWithSelenium, cls).tearDownClass()
        cls.selenium.quit()

    def test_exercice(self):

        selenium = self.selenium

        selenium.get('http://127.0.0.1:8000/login/')
        time.sleep(2)
        register_id = selenium.find_element_by_id('register_id')
        register_id.click()
        time.sleep(2)

        first_name = selenium.find_element_by_id('id_first_name')
        last_name = selenium.find_element_by_id('id_last_name')
        username = selenium.find_element_by_id('id_username')
        email = selenium.find_element_by_id('id_email')
        password1 = selenium.find_element_by_id('id_password1')
        password2 = selenium.find_element_by_id('id_password2')
        submit = selenium.find_element_by_id('register')

        username.send_keys('anass')
        time.sleep(2)
        first_name.send_keys('anass')
        time.sleep(2)
        last_name.send_keys('hamouch')
        time.sleep(2)
        email.send_keys('hamouch@gmail.com')
        time.sleep(2)
        password1.send_keys('hamouch')
        time.sleep(2)
        password2.send_keys('hamouch')

        time.sleep(3)
        submit.click()
        time.sleep(2)
        logout = selenium.find_element_by_id('logout')
        logout.click()
        time.sleep(3)

       
        username = selenium.find_element_by_id('id_username')
        password = selenium.find_element_by_id('id_password')
        submit = selenium.find_element_by_id('login')

        username.send_keys('anass')
        password.send_keys('hamouch')
        submit.click()
        time.sleep(3)

        submit1 = selenium.find_element_by_id('update_email')
        submit1.click()

        time.sleep(3)
        email = selenium.find_element_by_id('id_email')
        email.click()
        time.sleep(3)
        email.clear()
        time.sleep(3)
        email.send_keys('anass@ayomi.com')
        
        submit2 = selenium.find_element_by_id('update')
        submit2.click()
        time.sleep(2)






