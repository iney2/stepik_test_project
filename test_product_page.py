from .pages.product_page import ProductPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear)"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    page.test_guest_can_add_product_to_basket()
    page.test_book_name_match_with_book_name_in_basket()
    page.test_book_price_match_with_book_price_in_basket()

