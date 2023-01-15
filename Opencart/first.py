from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestPractice:
    global driver
    def PracticeDemo(self):
        driver = webdriver.Chrome(executable_path="G:\SQA\Automation_practice\driver\chrome\chromedriver.exe")
        driver.implicitly_wait(5)
        # maximize windows
        driver.maximize_window()
        #open website
        driver.get("https://www.w3schools.com/")
        time.sleep(3)
        # select linkText
        linkText = driver.find_element(By.LINK_TEXT,'Videos')
        linkText.click()
        time.sleep(2)
        # click subscribe
        subClink = driver.find_element(By.ID, 'topbuttontext')
        subClink.click()
        time.sleep(3)
        # click logo
        logoClick = driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/div/a')
        logoClick.click()
        time.sleep(3)
        #close the registration page
        # closePage = driver.find_element(By.CSS_SELECTOR,'.TopBarMenuLegacy_buttonbar__BiRmn svg')
        # closePage.click()
        # time.sleep(3)
        # registration
        # userName = driver.find_element(By)
        # # back
        # driver.back()
        # time.sleep(2)
        # referesh
        driver.refresh()
        time.sleep(2)
        # page title print
        print(driver.title)
        #close bowser
        driver.close()


test = TestPractice()
test.PracticeDemo()