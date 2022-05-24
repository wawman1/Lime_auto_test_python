from selenium.webdriver.common.by import By

class UrlPageLocators():
    link_main = 'https://vetin.front.eclipseds.ru/users'
    link_auth = 'https://vetin.front.eclipseds.ru/sign-in'

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, 'div.sidebar__row > a[href="/sign-in"]:nth-child(3)')
    REGISTER_LINK = (By.CSS_SELECTOR, 'div.sidebar__row > a[href="/sign_up_register"]')
    PRIVACY_LINK = (By.CSS_SELECTOR, 'ul.sidebar-info-menu__list > li > a[href="/privacy"]')
    FEEDBACK_BUTTON = (By.CSS_SELECTOR, 'ul.sidebar-info-menu__list > li > button.feedback')
    FEEDBACK_MODAL = (By.CSS_SELECTOR, 'div.vfm__content > div.modal-complaint')
    ABOUT_LINK = (By.CSS_SELECTOR, 'ul.sidebar-info-menu__list > li > a[href="/about"]')

class LoginPageLocators():
    LOGIN_USERNAME = (By.CSS_SELECTOR, 'label.login__label > input[type="text"]')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, 'label.login__label > input[type="password"]')
    LOGIN_AUTH_BUTTON = (By.CSS_SELECTOR, 'button.login__submit')
    NAME_IN_PROFILE = (By.CSS_SELECTOR, 'div.sidebar-account__user-info > p')
 
