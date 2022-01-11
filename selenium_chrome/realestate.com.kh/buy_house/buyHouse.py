# get info paginetion

from selenium import webdriver
import pandas as pd
import json
import time

pageinations = 'https://www.realestate.com.kh/buy/house/'
property_list = []
total_property_list = []

new_index = 0 
driver = webdriver.Chrome()
driver.implicitly_wait(5)
# "latitude":11.689690503883618,"longitude":104.87842746322178,

for x in range(1,10):
  for pageination in pageinations:
    time.sleep(0.1)
    page_num = str(x)
    print("getting page --- : ",page_num)
    url = pageinations + "?page=" + page_num
    driver.get(url)
    # print("page::",url)
    propertys = driver.find_elements_by_class_name("copy-wrapper")
    # print ("default::::",propertys)
    for property in propertys:
      # time.sleep(1)
      # print("propertyArr:::",property)
      price = property.find_element_by_class_name("price")
      addr = property.find_element_by_class_name("address")
      when = property.find_element_by_class_name('listed ')
      proper_item = {
        'Price': price.text,
        'Address' : addr.text,
        'Update': when.text,
      }
      property_list.append(proper_item)
      # print("proper_item::",proper_item)
    break
  # break
# total_property_list = property_list.append(proper_item) + property_list.append(property_list)
with open('buy_house-property.json', 'w') as f:
  json.dump(property_list, f)
df = pd.DataFrame(property_list)
print("df::",df)
driver.quit()