from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# Open a webpage to test
url="https://www.mindrisers.com.np/online-admission"
driver.get(url)


driver.execute_script("window.scrollBy(0,600)")
time.sleep(5)

driver.maximize_window()
fullName=driver.find_element(By.ID,"full_name")
fullName.send_keys("Bikram Rana")
time.sleep(2)

email=driver.find_element(By.ID,"email")
email.send_keys("bikramrana@60gmail.com")
time.sleep(2)

MobileNo=driver.find_element(By.ID,"mobile_no")
MobileNo.send_keys("9865321444")
time.sleep(2)

College=driver.find_element(By.ID,"college")
College.send_keys("college")
time.sleep(2)


driver.execute_script("window.scrollBy(0,600)")
time.sleep(5)

qualification=driver.find_element(By.ID,"qualification")
qualification.click("bachelor running")
time.sleep(2)
course=driver.find_element(By.ID,"course")
course.selected"Quality Assurance Training in Nepal")
time.sleep(2)
shedule=driver.find_element(By.ID,"schedule")
shedule.is_selected("evening")
time.sleep(2)

time.sleep(5)
driver.quit()
