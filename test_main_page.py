from .pages.main_page import MainPage
import pytest

@pytest.mark.guest_user
@pytest.mark.guest_user_sidebar
def test_guest_can_go_to_login_page(browser, get_baseurl):
    link = get_baseurl
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.guest_user
@pytest.mark.guest_user_sidebar
def test_guest_can_go_to_register_page(browser, get_baseurl):
    link = get_baseurl
    page = MainPage(browser, link)
    page.open()
    page.go_to_register_page()

@pytest.mark.guest_user
@pytest.mark.guest_user_sidebar
def test_guest_can_go_to_privacy_page(browser, get_baseurl):
    link = get_baseurl
    page = MainPage(browser, link)
    page.open()
    page.go_to_privacy_page()

@pytest.mark.guest_user
@pytest.mark.guest_user_sidebar
def test_guest_can_open_feedback_modal(browser, get_baseurl):
    link = get_baseurl
    page = MainPage(browser, link)
    page.open()
    page.open_feedback_modal()

@pytest.mark.guest_user
@pytest.mark.guest_user_sidebar
def test_guest_can_go_to_about_page(browser, get_baseurl):
    link = get_baseurl
    page = MainPage(browser, link)
    page.open()
    page.go_to_about_page()
    