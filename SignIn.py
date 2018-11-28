#-*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait  import WebDriverWait
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get('http://test.qianbaocard.com:23480/manager/index.html')
time.sleep(5)
EC.title_contains("运营中心") #Use the title to determine if the page is open
print(EC.title_contains("运营中心"))

#element=driver.find_element_by_class_name("login-label")
#EC.visibility_of_element_located(element)#judge if the element is visible
locator=(By.CLASS_NAME,"login-label")
WebDriverWait(driver,10).until(EC.visibility_of_element_located(locator))
driver.close()
#driver.find_element_by_xpath("//*[@id='name']").send_keys("U2201501011000000002")
#driver.find_element_by_id("password").send_keys("12345678")
#driver.find_element_by_id("code").send_keys("1111")