from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def test_guest_can_add_product_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        link.click()
        BasePage.solve_quiz_and_get_code(self)

    def test_book_name_match_with_book_name_in_basket(self):
        assert self.browser.find_element(*ProductPageLocators.BOOK_NAME).text == self.browser.find_element(
            *ProductPageLocators.BOOK_NAME_IN_BASKET).text, "Book name in the basket is not correct"

    def test_book_price_match_with_book_price_in_basket(self):
        assert self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text == self.browser.find_element(
            *ProductPageLocators.BOOK_PRICE_IN_BASKET).text, "Book price in the basket is not correct"


