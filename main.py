# Tested on MacOS, need to install chromedriver
# brew install chromedriver
import config, time, sys
from selenium import webdriver
from openpyxl import load_workbook

# Finds element and then types
def find(eid, txt):
    finder = wd.find_element_by_id(eid)
    finder.send_keys(txt)
    return

# Finds and click
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
wd.get("https://mail.google.com/mail/u/0/#inbox?compose=new")
wd.send_keys("hello")
# TODO: Loop through spreadsheet
wb = load_workbook(filename = sys.argv[1])
sheet = wb['Sheet1']

for i in range(45):
    finder2.send_keys(sheet['C' + (i + 1)].value)
# Used for debugging
time.sleep(1)
wd.quit()
