from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_setup():
    global driver
    driver = webdriver.Chrome(executable_path="G:\SQA\Automation_practice\driver\chrome\chromedriver.exe")
    # maximum window
    driver.maximize_window()
    driver.implicitly_wait(5)
    time.sleep(2)
    print(driver.title)


def search_element():
    driver.get("https://www.startech.com.bd/")
    driver.find_element(By.NAME, 'search').send_keys('Keyboard')
    driver.find_element(By.CLASS_NAME, 'material-icons').click()
    time.sleep(5)
    print(driver.title)

def test_teardown():
    print('Test passed successful')
    time.sleep(5)
    driver.close()


test_setup()
search_element()
test_teardown()