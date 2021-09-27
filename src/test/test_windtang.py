import time
import json

from getpass import getpass
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


# Log into the Windtang website from the home page
# Expected: Login successful
def login_test():
    # Windtang credentials
    credentials = open("src/test/credentials", 'r')
    username = credentials.readline()
    print ("Username:", username)
    password = credentials.readline()
    if password == "":
        password = getpass("Enter Windtang password for {0}: ".format (username))

    temp_password = ('*' * (len(password)//2) ) + password[len(password)//2:]
        
    print ("Password:", temp_password)
    # driver.get('http://www.windtang.com/')
    
    capabilities = DesiredCapabilities.CHROME
    capabilities['goog:loggingPrefs'] = { 'browser':'ALL' }
    driver = webdriver.Chrome("src/test/chromedriver", desired_capabilities=capabilities)
    
    url = 'http://localhost:3000'
    driver.get(url)

    # wait the ready state to be complete
    WebDriverWait(driver=driver, timeout=10).until(
        lambda x: x.execute_script("return document.readyState === 'complete'")
    )
    
    time.sleep(2) # Let the user actually see something!

    # Login Button
    try:
        driver.find_element_by_name("login-button").click()
        print ("Login button found! Clicking on it...")
        
    except NoSuchElementException as e:
        print ("Login button not found!", e)
        driver.quit()

    # Login page
    
    # wait the ready state to be complete
    WebDriverWait(driver=driver, timeout=10).until(
        lambda x: x.execute_script("return document.readyState === 'complete'")
    )

    # Login box
    try:
        login_box = driver.find_element_by_name("login-box")
        print ("Login box found!", login_box)
        login_box.send_keys(username)
        print ("Entering username: ", username)
        
    except NoSuchElementException as e:
        print ("Login box not found!", e)
        driver.quit()

    # Password box
    try:
        password_box = driver.find_element_by_name("password-box")
        print ("Password box found!", password_box)
        password_box.send_keys(password)
        print ("Entering password: ", temp_password)
        
    except NoSuchElementException as e:
        print ("Password box not found!", e)
        driver.quit()
        
    # Submit button
    try:
        submit_button = driver.find_element_by_name("submit-button")
        print ("Submit button found! Clicking on it...", submit_button)
        submit_button.click()
        
    except NoSuchElementException as e:
        print ("Submit box not found!", e)
        driver.quit()
        
    print ("TEST SUCCESSFUL")
    time.sleep(2)
    pre = driver.find_element_by_tag_name("pre").text
    data = json.loads(pre)
    print(data)
    time.sleep(2)
    driver.quit()

login_test()