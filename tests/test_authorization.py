import pytest
from pages.base_page import BasePage
from src.config import BASE_URL, TRAVEL_URL
from src.data import TEST_DATA
from locators.locators import Locators


@pytest.mark.usefixtures("driver")
class TestMainFunctionality:
    def test_user_authorization(self, driver):
        driver.get(BASE_URL)
        page = BasePage(driver)
        page.click_element()
        page.enter_email(TEST_DATA["login"])
        page.enter_password(TEST_DATA["password"])
        page.click_login_button()
        page.wait_for_element_orders()

        assert BASE_URL in driver.current_url

    def test_create_individual_order(self, driver):
        driver.get(BASE_URL)
        page = BasePage(driver)
        page.click_element()
        page.enter_email(TEST_DATA["login"])
        page.enter_password(TEST_DATA["password"])
        page.click_login_button()
        page.wait_for_element_orders()
        page.click_create_request()
        page.enter_name_product()
        page.enter_link_product()
        page.enter_name()
        page.enter_phone()
        page.scroll_create_order_button()
        page.click_create_order_button()
        page.wait_for_element_success_message()

        assert driver.find_element(*Locators.SUCCESS_MESSAGE).is_displayed()

    def test_create_one_way_trip(self, driver):
        driver.get(TRAVEL_URL)
        page = BasePage(driver)
        page.click_create_travel_button()
        page.enter_departure_city_input()
        page.enter_destination_city_input()
        page.enter_data()
        page.click_add_travel_button()
        page.wait_for_element_success_message_register()

        assert driver.find_element(*Locators.SUCCESS_MESSAGE_REGISTER).is_displayed()
