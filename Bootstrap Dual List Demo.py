# Bootstrap Dual List Demo test automation script

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import random


# set up chromedriver
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

try:
    # open the page with the dual list box
    driver.get("https://www.lambdatest.com/selenium-playground/")
    driver.maximize_window()
    
    wait = WebDriverWait(driver, timeout=15)
    
    driver.implicitly_wait(5)
    
    title = driver.title
    print("Current page title is:", title)
    
    bootstrap_dual = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Bootstrap List Box']")))
    bootstrap_dual.click()
    
    driver.implicitly_wait(5)
    
    print("Current page title is:", driver.title)
    
    # search for the element
    dual_list1 = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='well text-right']//ul[@class='list-group sp_list_group mb-20 mt-10']")))
    print("Dual list box is present")
    dual_list1.text
    print("Dual list box text is:", dual_list1.text)
    
    search = driver.find_element(By.XPATH, "(//input[@placeholder='search'])[1]")
    available_items = dual_list1.text.split("\n")
    for elements in available_items:
        choice1 = random.choice(available_items)
    search.send_keys(choice1)
    print("Search text is:", choice1)
    search.send_keys(Keys.ENTER)
    
    driver.implicitly_wait(10)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//li[normalize-space()='"+choice1+"']"))).click()
    print("Selected item is:", choice1)
    
    # move selected item to the right list box
    move_right = driver.find_element(By.XPATH, '//*[@id="__next"]/section[3]/div/div/div/div/div/div[2]/button[2]')
    move_right.click()
    print("Moved item to the right list box")
    
    # check if the item is moved to the right list box
    dual_list2 = wait.until(EC.presence_of_element_located((By.XPATH, "(//ul[@class='list-group sp_list_group mb-20 mt-10'])[2]")))
    available_items1 = dual_list2.text.split("\n")
    if choice1 in available_items1:
        print("Item is moved to the right list box:", available_items1)
    else:
        print("Item is not moved to the right list box")
        
finally:
    # close the browser
    driver.quit()
        
        