from selenium.webdriver.common.by import By

class Locators:
    LOGIN_BUTTON = (By.XPATH, "//a[@href='/ru-ru/sign-in?return_url=/ru-ru']")
    EMAIL_INPUT = (By.XPATH, "//input[@placeholder='Email или номер телефона']")
    PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='Пароль']")
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")
    ORDERS_BUTTON = (By.XPATH, "//span[text()='Заказы']")
    CREATE_REQUEST_BUTTON = (By.XPATH, "//a[text()='Оформить индивидуальный заказ']")
    NAME_PRODUCT_INPUT = (By.XPATH, "//input[@placeholder='Название товара *']")
    LINK_PRODUCT_INPUT = (By.XPATH, "//input[@placeholder='Ссылка на товар']")
    NAME_INPUT = (By.XPATH, "//input[@placeholder='Имя *']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='1 (702) 123-4567']")
    CREATE_ORDER_BUTTON = (By.XPATH, "//button[text()='Создать заявку']")
    SUCCESS_MESSAGE = (By.XPATH, "//p[text()='Состав заказа']")
    #travel
    CREATE_TRAVEL_BUTTON = (By.XPATH, "//a[text()='Создать поездку']")
    GOOGLE_SUGGESTIONS = (By.CSS_SELECTOR, ".pac-container .pac-item")
    DEPARTURE_CITY_INPUT = (By.XPATH, "//input[@placeholder='Откуда']")
    DESTINATION_CITY_INPUT = (By.XPATH, "//input[@placeholder='Куда']")
    DATA_INPUT = (By.XPATH, "//input[@placeholder='Когда']")
    ADD_TRAVEL_BUTTON = (By.XPATH, "//button[text()='Добавить поездку']")
    SUCCESS_MESSAGE_REGISTER = (By.XPATH, "//div[text()='Зарегистрироваться']")



