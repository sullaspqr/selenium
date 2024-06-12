from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.set_window_size(1920, 1080)

driver.get("https://www.python.org")
driver.save_screenshot('screenshot1.png')
time.sleep(3)
elem = driver.find_element(By.LINK_TEXT, value="Success Stories")
if not(elem.is_displayed()):
    print("Az elem nem jelenik meg az oldalon")
else:
    print("Az elem megjelenik az oldalon")
elem.click()
driver.save_screenshot('success.png')

time.sleep(3)
driver.quit()