from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pprint
import time as m

options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
chrome_browser = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))

chrome_browser.maximize_window()
chrome_browser.get("") # put your url here

get_to = chrome_browser.find_element(By.ID,"") # you can use id or name or xpath or class_name
get_to.click() 
m.sleep(1)
get_to.send_keys('') # this is the text you want to enter

chrome_browser.close() # when you are done, close the browser

# pip install selenium
# https://selenium-python.readthedocs.io/installation.html
