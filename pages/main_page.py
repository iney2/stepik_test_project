from pages.base_page import BasePage
from pages.locators import MainPageLocators
from pages.login_page import LoginPage


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)


    # def go_to_login_page(self):
    #     link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
    #     link.click()
    #     # return LoginPage(browser=self.browser, url=self.browser.current_url)
    #
    #     # login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
    #     # login_link.click()
    #
    # def should_be_login_link(self):
    #     assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
