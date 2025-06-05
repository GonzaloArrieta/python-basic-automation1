from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://duckduckgo.com/")

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("loopstation Zenith")
search_box.send_keys(Keys.RETURN)

time.sleep(3)

driver.save_screenshot("duckduckgo_result.png")

results = driver.find_elements(By.CSS_SELECTOR, "h2 a")
for result in results:
    print(result.text)

driver.quit()