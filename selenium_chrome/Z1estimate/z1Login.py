from selenium import webdriver
import pandas as pd
import json
import time
import json
import requests
import urllib.request as urllib2
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
chrome_options = Options()
chrome_options.add_argument("--no-sandbox") # linux only

new_index = 0 
driver = webdriver.Chrome()
driver.implicitly_wait(5)
FEM_ANY = driver.find_element

url = 'https://demo.z1datarnd.com/signin'
driver.get(url)
var_check = FEM_ANY(By.CSS_SELECTOR, "[data-test='login-form']")

if var_check:
  print('true')
  var_name = FEM_ANY(By.NAME,'email')
  var_passwd = FEM_ANY(By.NAME, 'password')
  var_submit = FEM_ANY(By.CSS_SELECTOR, "[type='submit']")
  # login
  var_name.send_keys("0962572064")
  var_passwd.send_keys("Zngounse71")
  var_submit.click()
  driver.implicitly_wait(5)
  # time.sleep(10)
  # search location
  var_btn_point = FEM_ANY(By.CSS_SELECTOR, "[id='id-z1estimate-point']")
  var_search = FEM_ANY(By.CSS_SELECTOR, "[placeholder='Search Z1Data Maps']")
  
  var_btn_point.click()
  var_search.send_keys("11.5353816,104.8040408")
  var_search.send_keys(Keys.ENTER)
  var_search.send_keys(Keys.ENTER)
  
  # wait 1 min
  time.sleep(6000)
else: 
  print("false")
# driver.quit