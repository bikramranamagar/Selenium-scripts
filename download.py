from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# Open a webpage to test
url="https://filebin.net"
driver.get(url)


driver.execute_script("window.scrollBy(0,600)")
time.sleep(5)
driver.maximize_window()

upload_fils=driver.find_element(*(By.XPATH,"//input[@id='fileField']"))
upload_fils.send_keys("C:/Users/Acer/OneDrive/Pictures/Screenshots/admin dashboard.png")
time.sleep(2)

more=driver.find_element(*(By.XPATH,"//a[@id='dropdownFileMenuButton']"))
more.click()

time.sleep(10)
driver.quit()
