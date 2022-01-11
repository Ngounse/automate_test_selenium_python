from selenium import webdriver
import pandas as pd
import json
import time
import json
import requests
import urllib.request as urllib2
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
chrome_options = Options()
# chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox") # linux only
# chrome_options.add_argument("--headless")
# chrome_options.headless = True # also works

import utils # BUY_HOUSE

BUY_HOUSE = utils.BUY_HOUSE
property_list = []
new_index = 0 
driver = webdriver.Chrome()
driver.implicitly_wait(0.1)
# driver.maximize_window()
# FEM_ID = driver.find_elements_by_id
# FEM_CLASS = driver.find_element_by_class_name
# FEM_XP = driver.find_element_by_xpath
FEM_ANY = driver.find_element
save_file_name = 'detail_buy_house1.4'

for pageDetail in BUY_HOUSE:
  img_arr = []
  url = pageDetail
  driver.get(url)
  property_check = FEM_ANY(By.ID, "overview")
  new_index += 1
  str_num = str(new_index)
  time.sleep(0.1)
  if property_check:
    print( str_num + " True_ === getting "+pageDetail+" property ===")
  # for pageDetail in BUY_HOUSE:
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'html.parser')
    res = soup.find('script')
    json_object = json.loads(res.contents[0])
    all_scripts = soup.find_all('script')
    
    new_index_a = 0
    # img_src_arr = FEM_ANY(By.ID,'photos')
    # if img_src_arr:
    for x in range(0,5):
      img_num = str(x)
      if x == 0 :
        img_src = FEM_ANY(By.XPATH,'.//*[@id="photos"]/div[1]/a/img')
        print(x,"==",img_src.get_attribute("src"),'image001')
        result_img = img_src.get_attribute("src")
        # img_item = {
        #   'Image': result_img
        # }
        img_arr.append(result_img)
      else :
        try : 
          img_src = FEM_ANY(By.XPATH,'.//*[@id="photos"]/div[1]/div/a['+img_num+']/img')
          # //*[@id="photos"]/div[1]/div/a[1]/img
          # //*[@id="photos"]/div[1]/div/a[2]/img
          # //*[@id="photos"]/div[1]/div/a[3]/img
          # //*[@id="photos"]/div[1]/div/a[4]/img
          # print(x,"==",img_src.get_attribute("src"),"image004")
          result_img = img_src.get_attribute("src")
          # img_item = {
          #   'Image': result_img
          # }
          print("xxxxxxxxxx>>>>>>",x)
          img_arr.append(result_img)
        except :
          print(x,"==","false")
    data = json.loads(all_scripts[1].get_text())
  # --- getting details
    # print('--- second method ---')
    # declaration
    property_check = FEM_ANY(By.ID, "overview")
    name = FEM_ANY(By.XPATH, './/*[@id="overview"]/div[1]/div[1]/h1')
    address = FEM_ANY(By.XPATH, './/*[@id="overview"]/div[1]/div[1]/h2')
    try:
      prefix = FEM_ANY(By.CLASS_NAME, "prefix").text
      price = FEM_ANY(By.CLASS_NAME, "price-value").text
      dimension = FEM_ANY(By.CLASS_NAME, 'dimension').text
    except:
      prefix = 0
      price = 0
      dimension = 0
    
    propertyType = FEM_ANY(By.XPATH, './/*[@id="overview"]/div[4]/div/div/div[1]/div[2]/span[2]')
    title = FEM_ANY(By.XPATH, './/*[@id="overview"]/div[4]/div/div/div[2]/div[2]/span[2]')
    # agency = FEM_XP('.//*[@id="overview"]/div[4]/div/div/div[3]/div[2]/span[2]/a')
    propertyID = FEM_ANY(By.XPATH, './/*[@id="overview"]/div[4]/div/div/div[4]/div[2]/span[2]')
    
    proper_item = {
      "Property_Name" : name.text,
      "Address" : address.text,
      'Prefix' : prefix,
      'Price' : price,
      'Sql_m2' : dimension,
      'Property Type': propertyType.text,
      'Property ID' : propertyID.text,
      'Title': title.text,
      # 'Agency': agency.text,
      'Location' : data,
      'Image' : img_arr,
      'Url': url,
    }
    property_list.append(proper_item)
    with open(save_file_name+'_each.json', 'w') as f:
      json.dump(property_list, f)
      df = pd.DataFrame(property_list)
      df.to_csv (r''+save_file_name+'_csv.csv', index = False, header=True)
    # break
  else:
    print( str_num + " False === getting "+pageDetail+" property ===")
# with open(save_file_name+'_full.json', 'w') as f:
# 		json.dump(property_list, f)
df = pd.DataFrame(property_list)
# print("df::",df)
driver.quit()