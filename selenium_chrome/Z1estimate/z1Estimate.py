from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import utils # arr_locations

chrome_options = Options()
chrome_options.add_argument("--no-sandbox") # linux only
new_index = 0 
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
FEM_ANY = driver.find_element
ARR_LOCATIONS = utils.arr_locations

url = 'https://demo.z1datarnd.com/signin'
driver.get(url)
var_check = FEM_ANY(By.CSS_SELECTOR, "[data-test='login-form']")

def fun_login():## login
  var_name = FEM_ANY(By.NAME,'email')
  var_passwd = FEM_ANY(By.NAME, 'password')
  var_submit = FEM_ANY(By.CSS_SELECTOR, "[type='submit']")
  var_name.send_keys("0962572064")
  var_passwd.send_keys("Zngounse71")
  var_submit.click()
  time.sleep(5)
  
def fun_search_location(each_location):## search location
  try :
    var_search = FEM_ANY(By.CSS_SELECTOR, "[placeholder='Search Z1Data Maps']")
    var_search.send_keys(each_location)
    var_search.send_keys(Keys.ENTER)
    var_search.send_keys(Keys.ENTER)
    time.sleep(3)
  except Exception as err : print("Error ::")
def fun_clear_location():## clear location
  time.sleep(3)
  try : FEM_ANY(By.CSS_SELECTOR, "[data-test='btn-clear']").click()
  except Exception as err : print("Error ::::::")
  
def fun_get_estimate_point():## get point estimate
  time.sleep(0.3)
  try :FEM_ANY(By.CSS_SELECTOR, "[id='id-z1estimate-point']").click()
  except Exception as err: print("::: err")
  
def fun_get_estimate_form(wait):## get estimate form
  try : 
    print(' ===== try to click on map ===== ')## click on center map
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "mapboxgl-canvas"))).click()
    # wait.until(EC.element_to_be_clickable((By.XPATH, "//*[name()='canvas']"))).click()
  except Exception as err: print(' ===== false to click on map ===== ', err)
  
def fun_fill_estimate_form(*args, **kwargs):## fill estimate form
  # print(*args,'args')
  # print(args[0],'kwargs')
  try :
    var_property_type = FEM_ANY(By.NAME, "property_type")
    var_lot_type = FEM_ANY(By.NAME, "lot_type")
    var_land_width = FEM_ANY(By.NAME, "land_width")
    var_land_length = FEM_ANY(By.NAME, "land_length")
    var_year = FEM_ANY(By.NAME, "year")
   
    var_btn_submit = FEM_ANY(By.CSS_SELECTOR, "[type='submit']")
  
    var_property_type.send_keys(args[0])
    var_lot_type.send_keys(args[1])
    var_land_width.send_keys(args[2])
    var_land_length.send_keys(args[3])
  
    var_bldg_width = FEM_ANY(By.NAME, "bldg_width")
    var_bldg_length = FEM_ANY(By.NAME, "bldg_length")
    var_total_bed = FEM_ANY(By.NAME, "total_bed")
    var_total_ba = FEM_ANY(By.NAME, "total_ba")
    var_total_floor = FEM_ANY(By.NAME, "total_floor")
    
    var_total_floor.send_keys(args[4])
    var_bldg_width.send_keys(args[5])
    var_bldg_length.send_keys(args[6])
    var_total_bed.send_keys(args[11])
    var_total_ba.send_keys(args[12])
    var_year.send_keys(2021)
    time.sleep(0.3)
    var_btn_submit.click()
    time.sleep(1)
  except Exception as err : print(" err::::")
    # print(err, '\n ----- error fill form ----- ')
  
def fun_get_estimate_price():## get estimate price
  try:
    var_estimate_price = FEM_ANY(By.CSS_SELECTOR, 'strong')
    print(var_estimate_price.text)
  except Exception as err : print("err :")
  
def fun_close_estimate_form():## fill estimate form
  time.sleep(2)
  try: FEM_ANY(By.CSS_SELECTOR, "[data-test='close-form']").click()
  except Exception as err : print("Error cf::::")
  time.sleep(1)
  try: FEM_ANY(By.CSS_SELECTOR, "[data-test='btn-close']").click()
  except Exception as err : print("Error bc::::")
  
if var_check:
  print('true')
  fun_login()
  try:
    wait = WebDriverWait(driver, 5)
    for each_location in ARR_LOCATIONS:
      fun_get_estimate_point()
      fun_search_location(each_location['location'])
      fun_clear_location()
      fun_get_estimate_form(wait)
      # print(each_location)
      fun_fill_estimate_form(
        each_location['Type'],
        each_location['Lot_Type'],
        each_location['Land_Width'],
        each_location['Land_Length'],
        each_location['No_of_Floors'],
        each_location['Bldg_Width'],
        each_location['Bldg_Length'],
        each_location['Title_Deed'],
        each_location['Kitchen'],
        each_location['Living_Room'],
        each_location['Road_Size'],
        each_location['Bedroom'],
        each_location['Bathroom'])
      time.sleep(5)
      fun_get_estimate_price()
      fun_close_estimate_form()
      time.sleep(3)
    ## wait 1 min
    print("---- sleeping ----")
    time.sleep(60)
  except Exception as err :
    print(err)
    print(" ---- false to get estimate ---- ")
else : 
  print(" ---- false check for login ---- ")
driver.quit()