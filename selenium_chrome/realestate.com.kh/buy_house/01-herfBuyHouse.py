# get link each property

from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import json
import time

pageinations = 'https://www.realestate.com.kh/buy/house/'
property_list = []
total_property_list = []

new_index = 0 
driver = webdriver.Chrome()
driver.implicitly_wait(2.5)

for x in range(1,51):
	for pageination in pageinations:
		# time.sleep(0.1)
		page_num = str(x)
		url = pageinations + "?page=" + page_num
		print("getting page --- : ",page_num)
		driver.get(url)
		propertys = driver.find_elements(By.CLASS_NAME, "carousel-wrap")
		# for property in propertys:
		link = [elem.get_attribute('href') for elem in propertys]
		property_list = property_list + link
		# print(type(link))
		break
	# break
with open('herf_buy_house_v.0.0.1.json', 'w') as f:
	json.dump(property_list, f)
df = pd.DataFrame(property_list)
# print("df::",df)
driver.quit()