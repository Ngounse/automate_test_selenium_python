from selenium import webdriver
import pandas as pd
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait as wait

url = 'https://www.realestate.com.kh/rent/toul-kork/'

driver = webdriver.Chrome()
driver.implicitly_wait(5) 
driver.get(url)

propertys = driver.find_elements_by_class_name("copy-wrapper")

property_list = []
new_index = 0 
for property in propertys:
  # new_index += 1
  # str_num = str(new_index)
  print("property:::",property)
  price = property.find_element_by_class_name("price")
  addr = property.find_element_by_class_name("address")
  when = property.find_element_by_class_name('listed ')
  proper_item = {
  	'Price': price.text,
  	'Address' : addr.text,
		'Update': when.text,
	}
  property_list.append(proper_item)
   
df = pd.DataFrame(property_list)
print("df::",df)
driver.quit()