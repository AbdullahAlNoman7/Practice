from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class WebElement:
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path="G:\SQA\Automation_practice\driver\chrome\chromedriver.exe")
        # maximum window
        driver.maximize_window()
        driver.implicitly_wait(5)
        time.sleep(2)
        # url
        url = driver.get("https://www.startech.com.bd/")
        # url1 = driver.current_url
        # print(url1)
        # print title
        print(driver.title)
    def search_element(self):
        search = self.driver.find_element(By.ID,'search')
        search.send_keys('Keyboard')
        search_click = self.driver.find_element(By.CLASS_NAME,'material-icons')
        search_click.click()
        time.sleep(5)
        print(driver.title)
    def test_teardown(self):
        print('Test passed successful')
        time.sleep(5)
        driver.close()


Web = WebElement()
Web.test_setup()
Web.search_element()
Web.test_teardown()
