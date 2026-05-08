# main.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from getpass import getpass

class LoginPage:
    URL = "https://github.com/login"
    USERNAME_INPUT = (By.ID, "login_field")
    PASSWORD_INPUT = (By.ID, "password")
    SUBMIT_BUTTON = (By.NAME, "commit")
    DASHBOARD = (By.CSS_SELECTOR, "[aria-label='Dashboard']")
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        driver.get(self.URL)
    
    def enter_username(self, username):
        self.wait.until(EC.presence_of_element_located(self.USERNAME_INPUT)).send_keys(username)
    
    def enter_password(self, password):
        self.find_element(self.PASSWORD_INPUT).send_keys(password)
    
    def click_submit(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()
    
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def is_logged_in(self):
        try:
            self.wait.until(EC.presence_of_element_located(self.DASHBOARD))
            return True
        except:
            return False

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

try:
    login_page = LoginPage(driver)
    login_page.enter_username(input("Логин: "))
    login_page.enter_password(getpass("Пароль: "))
    login_page.click_submit()
    
    if login_page.is_logged_in():
        print("Успешный вход!")
    else:
        print("Ошибка входа")
except Exception as e:
    print(f"Ошибка: {e}")
finally:

    driver.quit()
