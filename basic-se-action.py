
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

def browser_open():
  driver = webdriver.Chrome(ChromeDriverManager().install())
  driver.implicitly_wait(10)

def open_page_by_url(url):
  driver.get(url)
