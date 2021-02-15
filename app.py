from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import geckodriver_autoinstaller
import time

class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/login')
        time.sleep(10)
        email = bot.find_element_by_name('session[username_or_email]')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(5)
    
    def like_tweet(self,hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q='+ hashtag +'&src=typed_query')
        time.sleep(5)
        for i in range(1,5):
            bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')    
            time.sleep(5)
            tweets = bot.find_elements_by_xpath('//a[contains(@href,"status")]')
            links = [elem.get_attribute('href') for elem in tweets]
            #print(links)
            for link in links:
                bot.get('https://twitter.com' + link)
                try:
                    bot.find_element_by_xpath('//div[contains(@aria-label,"Like")]').click()
                    time.sleep(30)
                except Exception as e:
                	#print(e.message)
                    time.sleep(60)

geckodriver_autoinstaller.install()
autobot = TwitterBot('login', 'password')
autobot.login()
autobot.like_tweet('#theoscars2021')
