from .locators import MainPageLocators
from .base_page import BasePage

class MainPage(BasePage): 
    def go_to_login_page(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "ссылка на авторизацию не найдена"
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        assert "/sign-in" in self.browser.current_url, "sign-in отсутствует в url"

    def go_to_register_page(self):
        assert self.is_element_present(*MainPageLocators.REGISTER_LINK), "ссылка на регистрацию не найдена"
        register_link = self.browser.find_element(*MainPageLocators.REGISTER_LINK)
        register_link.click()
        assert "/sign_up_register" in self.browser.current_url, "sign_up_register отсутствует в url"

    def go_to_privacy_page(self):
        assert self.is_element_present(*MainPageLocators.PRIVACY_LINK), "ссылка на пользовательское соглашение не найдена"
        privacy_link = self.browser.find_element(*MainPageLocators.PRIVACY_LINK)
        privacy_link.click()
        assert "/privacy" in self.browser.current_url, "privacy отсутствует в url"

    def open_feedback_modal(self):
        assert self.is_element_present(*MainPageLocators.FEEDBACK_BUTTON), "кнопка обратной связи не найдена"
        feedback_button = self.browser.find_element(*MainPageLocators.FEEDBACK_BUTTON)
        feedback_button.click()
        assert self.is_element_present(*MainPageLocators.FEEDBACK_MODAL), "модальное окно обратной связи не найдено"
    def go_to_about_page(self):
        assert self.is_element_present(*MainPageLocators.ABOUT_LINK), "ссылка на о 'проекте/контакты' не найдена"
        privacy_link = self.browser.find_element(*MainPageLocators.ABOUT_LINK)
        privacy_link.click()
        assert "/about" in self.browser.current_url, "about отсутствует в url"
        