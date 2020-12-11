import selenium 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
chromedriverpath = "C"
import requests
class twitter:
    def __init__(self):
        self.driver =  webdriver.Chrome(executable_path=chromedriverpath)
    def login(self):
        self.driver.get("https://twitter.com/login?lang=en")
        usn = self.driver.find_element_by_name("session[username_or_email]")
        usn.send_keys("**********")
        pwd = self.driver.find_element_by_name("session[password]")
        pwd.send_keys("********")
        pwd.send_keys(Keys.ENTER)
    def tweet(self):
        response = requests.get(url="https://zenquotes.io/api/random")
        data = response.json()
        quote = data[0]["q"]
        author = data[0]["a"]
        tweetm = f"#photography#iwd2019#cryptocurrency#happyeaster#womensday#pressforprogress#happybirthday\n{quote}\n by:{author}"
        tweets = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div')
        tweets.send_keys(tweetm)
        sendtweet = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        sendtweet.click()


bot = twitter()
bot.login()
for x in range(10):
    time.sleep(3)
    bot.tweet()
