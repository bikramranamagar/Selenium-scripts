from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up Chrome WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Check if Selenium WebDriver is running
if driver.session_id:
    print("Selenium WebDriver is running!")
else:
    print("Selenium WebDriver is NOT running!")

# Define URL
url = "https://www.google.com.np/"

# Open the URL
driver.get(url)
print("Opened URL:", driver.current_url)

# Wait for 5 seconds
time.sleep(5)

# Close the browser
driver.quit()
print("Browser closed successfully.")
