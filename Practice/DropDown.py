from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

class DropDown:
    def setUp(self):
        global driver
        driver = webdriver.Chrome(executable_path="G:\SQA\Automation_practice\driver\chrome\chromedriver.exe")
        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.get("https://demo.opencart.com/")
        time.sleep(3)
    def dropDown(self):
        select_desktop = driver.find_element(By.LINK_TEXT,'Desktops')
        select_desktop.click()
        time.sleep(2)
        mac = driver.find_element(By.XPATH,'//*[@id="narbar-menu"]/ul/li[1]/div/div/ul/li[2]/a')
        mac.click()
        time.sleep(2)
        #scroll page
        driver.execute_script("window.scroll(0,600)")
        #select mac iteam
        select_mac = driver.find_element(By.CSS_SELECTOR,'.product-thumb')
        select_mac.click()
        time.sleep(3)
        # scroll page untill contect not found
        foundIteam = driver.find_element(By.ID,'input-quantity')
        driver.execute_script("arguments[0].scrollIntoView()",foundIteam)
        # add more iteam
        clear_form = driver.find_element(By.ID,'input-quantity')
        clear_form.clear()
        time.sleep(2)
        clear_form.send_keys(3)
        # add to card
        add_to_card = driver.find_element(By.ID,'button-cart')
        add_to_card.click()
        time.sleep(3)

        print(driver.title)



dp1 = DropDown()
dp1.setUp()
dp1.dropDown()