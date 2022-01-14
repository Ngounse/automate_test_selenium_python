from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import  time
# import z1Estimate

chrome_options = Options()
chrome_options.add_argument("--no-sandbox") # linux only
new_index = 0 
driver = webdriver.Chrome()
url = 'https://www.youtube.com/'
for x in range(0,5):
  driver2 = webdriver.Chrome()
  x = 'https://www.google.com/'
  driver2.get(x)
  print(driver2.get(x),":::")
  # z1Estimate()
  # for i in range(0,5):
  #   driver3 = webdriver.Chrome()
  #   url3 = 'https://www.facebook.com/'
  #   driver3.get(url3)
  # # time.sleep(10)
  print("::: open driver :::", x)


# driver.quit()
