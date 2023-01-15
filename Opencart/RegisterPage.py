from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time


class Register:
    def setUp(self):
        global driver
        driver = webdriver.Chrome(executable_path="G:\SQA\Automation_practice\driver\chrome\chromedriver.exe")
        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.get("https://demo.opencart.com/")
        time.sleep(3)

    def registration(self):
        element = driver.find_element(By.LINK_TEXT, 'My Account')
        element.click()
        time.sleep(2)
        selectIteam = driver.find_element(By.LINK_TEXT, 'Register')
        selectIteam.click()
        time.sleep(2)
        """
        # scroll page
        # driver.execute_script("window.scrollBy(0,1000)")
        srcoll = driver.find_element(By.CLASS_NAME, 'form-check-input')
        driver.execute_script("arguments[0].scrollIntoView()", srcoll)
        time.sleep(1)
        #submit
        submitBtn = driver.find_element(By.XPATH,'//*[@id="form-register"]/div/div/button')
        submitBtn.click()
        time.sleep(2)
        # radio box check
        radioBox = driver.find_element(By.ID,'input-newsletter-yes').is_selected()
        print(radioBox)
        time.sleep(1)
        # checkbox check
        cehckBox = driver.find_element(By.CLASS_NAME,'form-check-input').is_selected()
        print(cehckBox)
        # print(driver.title)
        """

    def userInfo(self):

        # user filed
        firstUserName = driver.find_element(By.ID, 'input-firstname')
        listUserName = driver.find_element(By.ID, 'input-lastname')
        email = driver.find_element(By.ID, 'input-email')
        password = driver.find_element(By.ID, 'input-password')
        # user data pass
        firstUserName.send_keys('Hello')
        listUserName.send_keys('kitty')
        email.send_keys('12346@gmail.com')
        password.send_keys('4654sdaf')
        time.sleep(3)
        #scroll down
        driver.execute_script("window.scroll(0,500)")
        # submit
        submit = driver.find_element(By.CSS_SELECTOR,'button:not(:disabled), [type=button]:not(:disabled), [type=reset]:not(:disabled), [type=submit]:not(:disabled)')
        submit.click()
        time.sleep(2)
    def tearDown(self):
        print('Ok')
        driver.close()


Reg = Register()
Reg.setUp()
Reg.registration()
Reg.userInfo()
Reg.tearDown()
