from .base_page import BasePage
from .locators import LoginPageLocators
from selenium import webdriver

email = 's.burdin.eclipse@gmail.com6'
password = 'qwerty123'

class LoginPage(BasePage):
    def login_in(self):
        
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME), "инпут логина не найден"
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_USERNAME)
        login_email.send_keys(email)
        
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "инпут пароля не найден"
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)
        login_email.send_keys(password)

        assert self.is_element_present(*LoginPageLocators.LOGIN_AUTH_BUTTON), "кнопка войти не найдена"
        login_auth_button = self.browser.find_element(*LoginPageLocators.LOGIN_AUTH_BUTTON)
        login_auth_button.click()

        assert self.is_element_present(*LoginPageLocators.NAME_IN_PROFILE), "имя в профиле не найдено"
        name_in_profile = self.browser.find_element(*LoginPageLocators.NAME_IN_PROFILE)
        name_in_profile_text = name_in_profile.text
        
        assert name_in_profile_text == "Брэд Питт" , f'это не Брэд Питт, это {name_in_profile_text}'
