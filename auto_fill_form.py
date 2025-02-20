from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
import re
import random
import string


# Set up Chrome WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

url = "https://www.mindrisers.com.np/contact-us"
driver.get(url)
driver.maximize_window()


driver.execute_script("window.scrollBy(0,600)")
time.sleep(2)

name_field= driver.find_element(*(By.XPATH,"//label[normalize-space()='Name']"))
email_field = driver.find_element(*(By.XPATH,"//label[normalize-space()='Email']"))
phone_field = driver.find_element(*(By.XPATH,"//label[normalize-space()='Phone']"))

def is_valid_email(email):
    try:
        email_pattern="^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        
        if re.search(email_pattern,email):
            return False
    except Exception as e:
        print(e)
        return False
    
        #  Generaton of random input values
def generation_random_email():
    domain="autimation.com"
    email_length = 5
    random_string = ''.join(random.choices(string.ascii_lowercase) for  _ in range (email,email_length))
    email = random_string+ "@" +domain
    return email
        
def generation_name():
    return ''.join(random.choices(string.ascii_letters,k=8))
def generation_phone():
    return "+977_98" + ''.join(random.choices(string.ascii_digits,k=8))

name1=generation_name()
email=generation_random_email
phone=generation_phone

time.sleep(2)

name_field.send_keys(name1)


email_field.send_keys(email)


phone_field.send_keys(phone)

if is_valid_email(email):
    print("email valid")
else:
    print("email Invalid")

time.sleep(4)
driver.quit()


