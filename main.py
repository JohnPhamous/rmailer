# Tested on MacOS, need to install chromedriver
# brew install chromedriver
import config, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

def find(eid, txt):
    finder = wd.find_element_by_id(eid)
    finder.send_keys(txt)
    return

def click(eid):
    finder = wd.find_element_by_id(eid)
    finder.click()
    return

# create a config.py with your email credentials
gmail = "http://gmail.com"
username = config.gusername
password = config.gpassword
netid = config.gnetid
netpass = config.gnetpass

# Initiates web driver with Chrome's engine
wd = webdriver.Chrome()

# Goes to url
wd.get(gmail)

# Initial login screen
find("Email", username)
click("next")

# Rweb login
time.sleep(1)
find("username", netid)
find("password", netpass + "\n")

# Compose email
time.sleep(1)
finder2 = wd.find_elements_by_xpath('.//*[@id=":3w"]/div/div[1]/span/a')[0]
finder2.send_keys('c')

# Used for debugging
time.sleep(1)
wd.quit()
