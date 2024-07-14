from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from datetime import date
import os
import json

service  = Service(executable_path='chromedriver.exe') 
DRIVER = webdriver.Chrome(service=service)

def searchBar():
    searchField = DRIVER.find_element(By.CSS_SELECTOR, value= "input[id='search']")
    searchField.clear();
    searchField.send_keys('Bahubali OST')
    


def open_youtube():
    DRIVER.get('https://youtube.com')
    time.sleep(2)
    searchBar()
    time.sleep(4)
    input("Bot operation Completed. Press any Key...")
    DRIVER.close()
    
    



if __name__ == "__main__":
    open_youtube()
 