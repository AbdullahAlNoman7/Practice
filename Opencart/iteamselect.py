from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

class ItemSelect:
    def setUp(self):
        global driver
        driver = webdriver.Chrome(executable_path="G:\SQA\Automation_practice\driver\chrome\chromedriver.exe")
        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.get("https://demo.opencart.com/index.php?route=common/home&language=en-gb")
        time.sleep(3)
    def click_item(self):
        driver.implicitly_wait(5)
        driver.find_element(By.CSS_SELECTOR,'.product-thumb h4').click()
        time.sleep(3)


itm = ItemSelect()
itm.setUp()
itm.click_item()