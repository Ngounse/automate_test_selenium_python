from selenium import webdriver
import pandas as pd
import json
import time
import json
import urllib.request as urllib2
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox") # linux only
chrome_options.add_argument("--headless")
chrome_options.headless = True # also works

BUY_HOUSE = [
	"https://www.realestate.com.kh/buy/kep/villa-197759/",
  "https://www.realestate.com.kh/buy/srangae/dabest-properties-197643/",
  "https://www.realestate/boeung-tumpun-2/5-bed-6-bath-shophouse-197639/",
  "https://www.realestate/boeung-tumpun-2/9-bed-12-bath-shophouse-197637/",
  "https://www.realestate.com.kh/buy/ta-khmao/st21-197596/",
]

# BUY_HOUSE = utils.BUY_HOUSE
property_list = []
new_index = 0 
driver = webdriver.Chrome()
driver.implicitly_wait(2.5)
FEM_ID = driver.find_elements_by_id
FEM_CLASSS = driver.find_element_by_class_name
FEM_XP = driver.find_element_by_xpath

for pageDetail in BUY_HOUSE:
	url = pageDetail
	driver.get(url)
	req = Request(url, headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'})
	propertys = FEM_ID("overview")
	if propertys:
		print ("True")
	else:
		print ("False")
			# break
# print ("",pageDetail)