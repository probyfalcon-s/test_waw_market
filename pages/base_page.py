from selenium.webdriver.support.ui import WebDriverWait
from locators.locators import Locators
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click_element(self, timeout=15):
        element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(Locators.LOGIN_BUTTON))
        element.click()

    def enter_email(self, login, timeout=10):
        email_input = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(Locators.EMAIL_INPUT)
        )
        email_input.send_keys(login)

    def enter_password(self, password):
        self.driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*Locators.SUBMIT_BUTTON).click()

    def wait_for_element_orders(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(Locators.ORDERS_BUTTON)
        )
    #create_order
    def click_create_request(self):
        self.driver.find_element(*Locators.CREATE_REQUEST_BUTTON).click()

    def enter_name_product(self, timeout=10):
        create_request = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(Locators.NAME_PRODUCT_INPUT)
        )
        create_request.send_keys('test')

    def enter_link_product(self):
        self.driver.find_element(*Locators.LINK_PRODUCT_INPUT).send_keys('https://www.amazon.com/')

    def enter_name(self):
        self.driver.find_element(*Locators.NAME_INPUT).send_keys('test')

    def enter_phone(self):
        self.driver.find_element(*Locators.PHONE_INPUT).send_keys('0000000000')

    def scroll_create_order_button(self):
        element = self.driver.find_element(*Locators.CREATE_ORDER_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_create_order_button(self, timeout=15):
        create_order = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(Locators.CREATE_ORDER_BUTTON)
        )
        create_order.click()

    def wait_for_element_success_message(self, timeout=15):
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(Locators.SUCCESS_MESSAGE)
        )
    # create travel
    def click_create_travel_button(self):
        self.driver.find_element(*Locators.CREATE_TRAVEL_BUTTON).click()

    def enter_departure_city_input(self, timeout=10):
        departure_city = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(Locators.DEPARTURE_CITY_INPUT)
        )
        departure_city.send_keys('Тампа, Флорида, США')

    def enter_destination_city_input(self):
        self.driver.find_element(*Locators.DESTINATION_CITY_INPUT).send_keys('Москва, Россия')

    def enter_data(self):
        self.driver.find_element(*Locators.DATA_INPUT).send_keys('21.12.2024')

    def click_add_travel_button(self):
        self.driver.find_element(*Locators.ADD_TRAVEL_BUTTON).click()

    def wait_for_element_success_message_register(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(Locators.SUCCESS_MESSAGE_REGISTER)
        )

