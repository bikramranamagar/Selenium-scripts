from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the webpage
url = "https://www.mindrisers.com.np/online-admission"
driver.get(url)

# Scroll down
driver.execute_script("window.scrollBy(0,600)")
time.sleep(2)

driver.maximize_window()

# Fill out the form
fullName = driver.find_element(By.ID, "full_name")
fullName.send_keys("Bikram Rana")
time.sleep(2)

email = driver.find_element(By.ID, "email")
email.send_keys("bikramrana60@gmail.com")  # Fixed email format
time.sleep(2)

MobileNo = driver.find_element(By.ID, "mobile_no")
MobileNo.send_keys("9865321444")
time.sleep(2)

College = driver.find_element(By.ID, "college")
College.send_keys("My College Name")
time.sleep(2)

# Scroll to next section
driver.execute_script("window.scrollBy(0,600)")
time.sleep(2)

# Selecting Academic Status
AcademicStatus = Select(driver.find_element(By.ID, "qualification"))
AcademicStatus.select_by_visible_text("Bachelor Running")
time.sleep(2)

# Selecting Course
course = Select(driver.find_element(By.ID, "course"))
course.select_by_visible_text("Quality Assurance Training in Nepal")
time.sleep(2)

# Selecting Schedule
schedule = Select(driver.find_element(By.ID, "schedule"))
schedule.select_by_visible_text("Evening")
time.sleep(2)

# Wait before closing
time.sleep(5)
driver.quit()
