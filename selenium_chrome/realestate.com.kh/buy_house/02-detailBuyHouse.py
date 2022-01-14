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

BUY_HOUSE = utils.HERF_BUY_HOUSE
property_list = []
new_index = 0 
driver = webdriver.Chrome()
driver.implicitly_wait(0.1)
# driver.maximize_window()
FEM_ANY = driver.find_element
save_file_name = 'detail_buy_house_v0.0.2'

for pageDetail in BUY_HOUSE:
  img_arr = []
  
  url = pageDetail
  driver.get(url)
  try :
    ## --------------
    prop_bd = ''
    prop_ba = ''
    prop_floor = ''
    prop_sqm =''
    prop_floor_area = ''
    prop_land_area = ''
    ## --------------
    prop_type = ''
    prop_title = ''
    prop_ID = ''
    prop_original_ID = ''
    prop_listed = ''
    prop_updated = ''
    ## --------------
    property_check = FEM_ANY(By.ID, "overview")
    new_index += 1
    str_num = str(new_index)
    time.sleep(0.1)
    if property_check:
      print( str_num + " True_ === getting "+pageDetail+" property ===")
    ## for pageDetail in BUY_HOUSE:
      req = Request(url, headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'})
      webpage = urlopen(req).read()
      soup = BeautifulSoup(webpage, 'html.parser')
      res = soup.find('script')
      json_object = json.loads(res.contents[0])
      all_scripts = soup.find_all('script')
      
      new_index_a = 0
      for x in range(0,5):
        img_num = str(x)
        if x == 0 :
          img_src = FEM_ANY(By.XPATH,'.//*[@id="photos"]/div[1]/a/img')
          # print(x,"==",img_src.get_attribute("src"),'image001')
          result_img = img_src.get_attribute("src")
          img_arr.append(result_img)
        else :
          try : 
            img_src = FEM_ANY(By.XPATH,'.//*[@id="photos"]/div[1]/div/a['+img_num+']/img')
            result_img = img_src.get_attribute("src")
            img_arr.append(result_img)
          except :
            print(x,"==","false")
      data = json.loads(all_scripts[1].get_text())
    ## --- getting details
      # print('--- second method ---')
      ## declaration
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
        
      ## get Property Detail
      for x in range(0,10):
        str_num = str(x)
        try :
          view_title = FEM_ANY(By.XPATH, './/*[@id="overview"]/div[2]/div['+str_num+']/span[2]/span[2]').text
          view_value = FEM_ANY(By.XPATH, './/*[@id="overview"]/div[2]/div['+str_num+']/span[1]').text
          
          if view_title == 'Bedroom' : prop_bd = view_value
          if view_title == 'Bathroom' : prop_ba = view_value
          if view_title == 'Floor Area (m²)' : prop_floor_area = view_value
          if view_title == 'Land Area (m²)' : prop_land_area = view_value
          if view_title == 'Floor Level' : prop_floor = view_value
          # print(view_title,":",view_value)
        except Exception as err : i = 'err'
        # print(i, ":::")
        
      ## get Property Overview
      for x in range(0,10):
        str_num = str(x)
        try :
          overview_title = FEM_ANY(By.XPATH, './/*[@id="overview"]/div[4]/div[1]/div/div['+str_num+']/div[2]/span[1]').text
          overview_value = FEM_ANY(By.XPATH, './/*[@id="overview"]/div[4]/div[1]/div/div['+str_num+']/div[2]/span[2]').text
          #       ## --------------
          # prop_type = ''
          # prop_title = ''
          # prop_ID = ''
          # prop_original_ID = ''
          # prop_listed = ''
          # prop_updated = ''
          # ## --------------
          if overview_title == 'Property type:' : prop_type = overview_value
          if overview_title == 'Title:' : prop_title = overview_value
          if overview_title == 'Property ID:' : prop_ID = overview_value
          if overview_title == 'Original ID:' : prop_original_ID = overview_value
          if overview_title == 'Listed:' : prop_listed = overview_value
          if overview_title == 'Updated:' : prop_updated = overview_value
          # print(overview_title,":",overview_value)
        except Exception as err : i = 'err'
        # print(i, ":::")
      proper_item = {
        "Property_Name" : name.text,
        "Address" : address.text,
        'Prefix' : prefix,
        'Price' : price,
        'Sql_m2' : dimension,
        'Property Type': prop_type,
        'Property ID' : prop_ID,
        'Title' : prop_title,
        'Original ID' : prop_original_ID,
        'Listed' : prop_listed,
        'Updated' : prop_updated,
        'Bedroom' : prop_bd,
        'Bathroom' : prop_ba,
        'Floor_Area' : prop_floor_area,
        'Land_Area' : prop_land_area,
        'Floor': prop_floor,
        'Image' : img_arr,
        'Location' : data,
        'Url': url,
      }
      property_list.append(proper_item)
      with open(save_file_name+'_each.json', 'w') as f:
        json.dump(property_list, f)
        df = pd.DataFrame(property_list)
        df.to_csv (r''+save_file_name+'_csv.csv', index = False, header=True)
      # break
    else:
      proper_item = {
        'Url': url,
      }
      with open(save_file_name+'_each_fail.json', 'w') as f:
        json.dump(property_list, f)
        df = pd.DataFrame(property_list)
        df.to_csv (r''+save_file_name+'_csv_fail.csv', index = False, header=True)
      print( str_num + " False === getting "+pageDetail+" property ===")
  except Exception as err : 
    print(err,"err :::")
    proper_item = {
        'Url': url,
      }
    with open(save_file_name+'_each_fail.json', 'w') as f:
      json.dump(property_list, f)
      df = pd.DataFrame(property_list)
      df.to_csv (r''+save_file_name+'_csv_fail.csv', index = False, header=True)
    print( str_num + " False === getting "+pageDetail+" property ===")
# with open(save_file_name+'_full.json', 'w') as f:
# 		json.dump(property_list, f)
df = pd.DataFrame(property_list)
# print("df::",df)
driver.quit()