from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.set_window_size(1920, 1080)

driver.get("https://szallas.sulla.hu/")
driver.find_element(By.XPATH, '//input[@name="email"]').send_keys('user@kodbazis.hu')
time.sleep(1)
driver.find_element(By.XPATH, '//input[@name="password"]').send_keys('teszt')
time.sleep(1)
#driver.find_element(By.XPATH, '//input[@name="password"]').clear()
driver.find_element(By.TAG_NAME, 'button').click()
driver.save_screenshot('screenshot.png')
time.sleep(2)
driver.quit()
