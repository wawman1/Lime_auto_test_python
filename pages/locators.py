from selenium.webdriver.common.by import By

class UrlPageLocators():
    link_main = 'https://vetin.front.eclipseds.ru/users'
    link_auth = 'https://vetin.front.eclipseds.ru/sign-in'

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "div.sidebar__row > a[href='/sign-in']:nth-child(3)")

class LoginPageLocators():
    LOGIN_USERNAME = (By.CSS_SELECTOR, 'label.login__label > input[type="text"]')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, 'label.login__label > input[type="password"]')
    LOGIN_AUTH_BUTTON = (By.CSS_SELECTOR, 'button.login__submit')
    NAME_IN_PROFILE = (By.CSS_SELECTOR, 'div.sidebar-account__user-info > p')
 
