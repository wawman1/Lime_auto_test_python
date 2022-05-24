from .pages.main_page import MainPage
from .pages.locators import UrlPageLocators
import pytest

@pytest.mark.guest_user
def test_guest_can_go_to_login_page(browser):
    link = UrlPageLocators.link_main
    page = MainPage(browser, link)   
    page.open()                      
    page.go_to_login_page()         
