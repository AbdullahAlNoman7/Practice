from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class ClassTest:

    def setUp(self):
        global driver
        driver = webdriver.Chrome(executable_path="G:\SQA\Automation_practice\driver\chrome\chromedriver.exe")
        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.get("https://www.w3schools.com/")
        time.sleep(3)

    def clickLinkText(self):
        linkText = driver.find_element(By.LINK_TEXT, 'Videos')
        linkText.click()
        time.sleep(2)

    def clikSub(self):
        clickSub = driver.find_element(By.ID, 'topbuttontext')
        clickSub.click()
        time.sleep(2)

    def registration(self):
        userName = driver.find_element(By.NAME, 'email')
        password = driver.find_element(By.NAME, 'current-password')
        showPass = driver.find_element(By.CLASS_NAME, 'PasswordInput_show_pwd_btn__Ncc9S')
        logIn = driver.find_element(By.CSS_SELECTOR, '.Button_button__URNp\+.Button_primary__d2Jt3')
        userName.send_keys('hello@gmail.com')
        password.send_keys('131564')
        showPass.click()
        time.sleep(2)
        logIn.click()
        time.sleep(2)
    def fieldCheck(self):
        userNameCheck = driver.find_element(By.NAME, 'email')
        passwordCheck = driver.find_element(By.NAME, 'current-password')
        print(userNameCheck.is_displayed())
        print(userNameCheck.is_enabled())
    def tearDown(self):
        print('Successfully done')
        driver.close()


test1 = ClassTest()
test1.setUp()
test1.clickLinkText()
test1.clikSub()
test1.registration()
test1.tearDown()
