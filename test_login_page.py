from .pages.login_page import LoginPage
from .pages.locators import UrlPageLocators
import pytest

@pytest.mark.smoke
def test_guest_login_in(browser):
    link = UrlPageLocators.link_auth
    page = LoginPage(browser, link)   
    page.open()
    page.login_in()

