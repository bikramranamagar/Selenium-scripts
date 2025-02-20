from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# Open a webpage to test
url="https://formy-project.herokuapp.com/form"
driver.get(url)

driver.maximize_window()
firstName=driver.find_element(By.ID, "first-name")
firstName.send_keys("Bikram")
time.sleep(2)

lastName=driver.find_element(By.ID,"last-name")
lastName.send_keys("Rana")
time.sleep(2)

Jobtitle=driver.find_element(By.ID,"job-title")
Jobtitle.send_keys("QA intent")
time.sleep(2)

highschoollevel=driver.find_element(By.ID,"radio-button-1")
highschoollevel.send_keys("College")
time.sleep(2)

sex=driver.find_element(By.ID,"checkbox-2")
sex.click("male")
time.sleep(2)

yearofexperience=driver.find_element(By.ID,"select-menu")
yearofexperience.clear("/html/body/div/form/div/div[6]/select/option[2]")
time.sleep(2)

# scrolldown
driver.execute_script("window.scrollBy(0,600)")
time.sleep(2)


time.sleep(5)
driver.quit()

