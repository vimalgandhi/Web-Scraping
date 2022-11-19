from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os


load_dotenv()
options = Options()

driver = webdriver.chrome(
    os.getenv('PATH'), options=Options)
driver.get('https://opensea.io/collection/boredapeyachtclub')
time.sleep(3)
a = driver.find_element_by_tag('body')
while True:
    a.send_keys(Keys.PAGE_DOWN)
    time.sleep(3)
