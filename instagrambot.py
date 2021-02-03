import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
CHROME_DRIVER_PATH = ""
USERNAME = "*"
PASSWORD = "*"
tag = "programming"
class bot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)

        usn = self.driver.find_element_by_name("username")
        pwd = self.driver.find_element_by_name("password")
        usn.send_keys(USERNAME)
        pwd.send_keys(PASSWORD)
        time.sleep(2)
        pwd.send_keys(Keys.ENTER)
    def like(self):
        time.sleep(5)
        self.driver.get("https://www.instagram.com/explore/tags/programming/")
        post = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div[1]/div[2]')
        post.click()
        time.sleep(2)
        for x in range(100):
            likebutton = self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button')
            likebutton.click()
            nextpost = self.driver.find_element_by_class_name("coreSpriteRightPaginationArrow")
            nextpost.click()
            time.sleep(1)
bot1 = bot()
bot1.login()
bot1.like()
