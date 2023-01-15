from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time

class ActionChain:
    def setUp(self):
        global driver
        driver = webdriver.Chrome(executable_path="G:\SQA\Automation_practice\driver\chrome\chromedriver.exe")
        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.get("https://www.daraz.com.bd/#")
        time.sleep(2)
    """
    def closePopUp(self):
        time.sleep(10)
        deny = driver.find_element(By.CSS_SELECTOR,'.airship-btn:first-child')
        deny.click()
        # time.sleep(10)
    """
    def changeLanguage(self):
        """
        language_change = driver.find_element(By.XPATH,'//*[@id="topActionSwitchLang"]/span')
        language_change.click()
        time.sleep(2)
        #select language
        select_language = driver.find_element(By.XPATH,'//*[@id="lzdSwitchPop"]/div/div[2]/text()')
        select_language.click()
        time.sleep(2)
        """
    def actionChain(self):
        # mouse over
        action_over = ActionChains(driver)
        women_fashin = driver.find_element(By.XPATH,'//*[@id="Level_1_Category_No1"]/a/span')
        action_over.move_to_element(women_fashin).perform()
        time.sleep(1)
        clothing = driver.find_element(By.XPATH,'//*[@id="J_3442298940"]/div/ul/ul[1]/li[1]/a/span')
        action_over.move_to_element(clothing).perform()
        time.sleep(1)
        sarees = driver.find_element(By.XPATH,'//*[@id="J_3442298940"]/div/ul/ul[1]/li[1]/ul/li[6]/a/span')
        action_over.move_to_element(sarees).click().perform()

    def selectSarees(self):
        checkBox = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[3]/div[1]/div/div[2]/div/div[2]/div[2]/div/div/label[1]/span[2]')
        checkBox.click()
        time.sleep(2)
        # select price range
        minRange = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div/div/div[2]/div/div[5]/div[2]/div/input[1]')
        maxRange = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div/div/div[2]/div/div[5]/div[2]/div/input[2]')
        clickBtn = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div/div/div[2]/div/div[5]/div[2]/div/button')
        # send action
        minRange.send_keys(350)
        maxRange.send_keys(3000)
        clickBtn.click()
        time.sleep(3)
        #select sarees
        select_sarees = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div/div/div[1]/div[3]/div[26]/div/div/div[2]/div[2]/a')
        select_sarees.click()
        time.sleep(2)
        #How many item select
        item = driver.find_element(By.XPATH,'//*[@id="module_quantity-input"]/div/div/div/div/div[1]/a[1]/span/i')
        item.click()
        time.sleep(3)
        # add to cart
        addToCard = driver.find_element(By.XPATH,'//*[@id="module_add_to_cart"]/div/button[2]/span/span')
        addToCard.click()
        time.sleep(3)
        # close popup Window
        popUp = driver.find_element(By.XPATH,'/html/body/div[10]/div/div[2]/a/i')
        popUp.click()

    def tearDown(self):
        print('Tested')
        driver.close()


action = ActionChain()
action.setUp()
# action.closePopUp()
# action.changeLanguage()
action.actionChain()
action.selectSarees()
# action.selectSareesIteam()
action.tearDown()