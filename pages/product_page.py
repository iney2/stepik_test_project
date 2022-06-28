from pages.base_page import BasePage
from pages.locators import ProductPageLocators


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

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_should_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def no_goods_in_the_basket(self):
        assert self.is_disappeared(*ProductPageLocators.GOODS_IN_THE_BASKET), \
            "Success message is presented, but should not be"

    def basket_is_empty_message_exist(self):
        assert self.is_not_element_present(*ProductPageLocators.BASKET_IS_EMPTY), \
            "Basket is empty"