from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
CHROME_PATH="YOUR PATH"
PROMISED_DOWN="YOUR PROMISED DOWN"
PROMISED_UP="YOUR PROMISED DOWN"
TWITTER_USERNAME="YOUR EMAIL/USERNAME"
TWITTER_PASSWORD="PASSWORD"

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver=webdriver.Chrome(executable_path=CHROME_PATH)
        self.down=PROMISED_DOWN
        self.up=PROMISED_UP


    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.consent=self.driver.find_element_by_xpath('//*[@id="_evidon-banner-acceptbutton"]')
        self.consent.click()
        self.go_button=self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        self.go_button.click()
        sleep(60)
        self.REAL_DOWN=self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.REAL_UP=self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
        # print(f"DOWNLOAD: {self.REAL_DOWN}  UPLOAD:{self.REAL_UP}")



    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        sleep(5)
        email=self.driver.find_element_by_name("username")
        email.send_keys(TWITTER_USERNAME)
        email.send_keys(Keys.ENTER)
        sleep(5)
        password=self.driver.find_element_by_name("password")
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)
        sleep(5)
        tweet=self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div')
        tweet.click()
        #example of message for this project
        tweet.send_keys(f"Hello -PROVIDER NAME-. Why is my internet speed {self.REAL_DOWN}down/{self.REAL_UP}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up? ")
        tweet_button=self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        sleep(2)
        tweet_button.click()
        sleep(1)
        self.driver.quit()



test=InternetSpeedTwitterBot()
test.get_internet_speed()
test.tweet_at_provider()






