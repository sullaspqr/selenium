from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.set_window_size(1920, 1080)

driver.get("https://www.python.org/downloads/")
driver.save_screenshot('screenshot.png')
elements = driver.find_elements(By.CLASS_NAME, 'release-download')
time.sleep(1)
for e in elements:
    print(e.text)
