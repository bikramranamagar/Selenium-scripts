from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open a webpage to test
url="https://meroshare.cdsc.com.np/#/login"
driver.get(url)

driver.maximize_window()
time.sleep(2)
Select_dp=driver.find_element(By.ID,"select2-sxvf-container")
