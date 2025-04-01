from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def run_login_test():
    driver = webdriver.Chrome()  # Launch Chrome
    driver.get("https://www.netflix.com/in/login")  # Open the login page

    username = driver.find_element(By.ID, "email")  # Find email field
    password = driver.find_element(By.ID, "password")  # Find password field
    
    username.send_keys("testuser@example.com")  # Enter email
    password.send_keys("SecurePass123")  # Enter password
    password.send_keys(Keys.RETURN)  # Press Enter

    time.sleep(2)  # Wait for the page to load

    if "dashboard" in driver.current_url:
        print("Test Passed: Login successful")
    else:
        print("Test Failed: Login failed")

    driver.quit()  # Close the browser

run_login_test()
