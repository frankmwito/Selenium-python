from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# set up chromedriver
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

try:
    # navigate to the page with the form
    driver.get("https://www.lambdatest.com/selenium-playground/")
    driver.maximize_window()
    
    wait = WebDriverWait(driver, timeout=10)
    
    form = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Ajax Form Submit")))
    form.click()
    
    # wait for the form to be present
    
    print("Current page title is:", driver.title)
        
    # fill out the form
    
    name = wait.until(EC.presence_of_element_located((By.NAME, "title")))
    name.send_keys("Selenium")
    
    message = wait.until(EC.presence_of_element_located((By.ID, "description")))
    message.send_keys("I am going to have a house in south B or C at before 2025")
    
    sumit_button = driver.find_element(By.ID, "btn-submit")
    sumit_button.click()
    
    # wait for the success  message to be present
    success_message = wait.until(EC.presence_of_element_located((By.ID, "submit-control")))
    print("Success message is:", success_message.text)
    
    if "Form submitted Successfully!" in success_message.text:
        print("Success message is correct")
    else:
        print("Success message is incorrect")
    
finally:
    
    # close the browser
    driver.quit()
