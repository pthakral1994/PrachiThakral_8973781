import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Start a new instance of Chrome WebDriver
driver = webdriver.Chrome()

# Open the Dollarama website
driver.get("https://www.dollarama.com/")

# Wait for the page to load
wait = WebDriverWait(driver, 10)
wait.until(EC.title_contains("Dollarama"))

time.sleep(5)
# Element-1 Find sign in/registration Tab
SignIn_Tab = driver.find_element("xpath","/html/body/header/nav/div[1]/div/header-widget/div/a[1]")
SignIn_Tab.click()

# Wait for demonstration purposes
time.sleep(3)   # Wait for search results to load

# Element-2 Find the email input field and enter the email address
email_input = driver.find_element("xpath","/html/body/div[3]/login-section/div/div[1]/div[2]/form/div[1]/input")
email_input.send_keys("thakralprachi@gmail.com")

# Wait for demonstration purposes
time.sleep(3)   # Wait for search results to load

# Element-3 Enter "password" in password field
password_field = driver.find_element("xpath", "/html/body/div[3]/login-section/div/div[1]/div[2]/form/div[2]/input")
password_field.send_keys("Asdf@123")
time.sleep(3)  # Wait for search results to load

# Element-4 Find the Sign-in button and click it
SignIn_button = driver.find_element("xpath","/html/body/div[3]/login-section/div/div[1]/div[2]/button")
SignIn_button.click()

# Wait for the page to load
time.sleep(3)   # Wait for search results to load

# Element-5 : Click on the career tab
career_tab = driver.find_element("xpath","/html/body/header/nav/div[2]/div[1]/div[1]/div[6]/a")
career_tab.click()

time.sleep(3)  # Wait for search results to load

# Element-6 Click on the teamleader job button
Teamleader_button = driver.find_element("xpath","/html/body/div[2]/div[1]/div[3]/div/div/div[1]/div[1]/div[1]/div/div/div/div[2]/div/button")
Teamleader_button.click()

time.sleep(3)  # Wait for search results to load

# Close the WebDriver session
driver.quit()