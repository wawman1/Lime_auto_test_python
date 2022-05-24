from .locators import MainPageLocators
from .base_page import BasePage

class MainPage(BasePage): 
    def go_to_login_page(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "ссылка на авторизацию не найдена"
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
