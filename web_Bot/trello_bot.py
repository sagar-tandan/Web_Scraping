from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
from datetime import date
import os
import json

service = Service(executable_path='chromedriver.exe')
DRIVER = webdriver.Chrome(service=service)
        
        
def login():
    with open('config.json') as configfile:
        credentials = json.load(configfile)
        print(credentials)
        time.sleep(2)
        DRIVER.find_element(By.XPATH, value="//a[@href='https://id.atlassian.com/login?application=trello&continue=https%3A%2F%2Ftrello.com%2Fauth%2Fatlassian%2Fcallback%3Fdisplay%3DeyJ2ZXJpZmljYXRpb25TdHJhdGVneSI6InNvZnQifQ%253D%253D&display=eyJ2ZXJpZmljYXRpb25TdHJhdGVneSI6InNvZnQifQ%3D%3D']").click()
        time.sleep(2)
        username = DRIVER.find_element(By.CSS_SELECTOR,value="input[name='username']")
        username.clear()
        username.send_keys(credentials["USERNAME"])
        time.sleep(2)
        DRIVER.find_element(By.CSS_SELECTOR, value = "button[id = 'login-submit']").click()
        time.sleep(2)
        password = DRIVER.find_element(By.CSS_SELECTOR, value= "input[name = 'password']")
        password.clear()
        password.send_keys(credentials["PASSWORD"])
        time.sleep(2)
        DRIVER.find_element(By.CSS_SELECTOR, value = "button[id = 'login-submit']").click()
        # time.sleep(8)
        # DRIVER.find_element(By.CSS_SELECTOR, value = "button[id ='mfa-promote-dismiss']").click()
        time.sleep(5)

def navigateToBoard():
    DRIVER.find_element(By.XPATH, value= "//a[@href='/b/CeGTMO68/bot-board']").click()
    time.sleep(5)
    
def addTask():
    DRIVER.find_element(By.CSS_SELECTOR,value="button[data-testid = 'list-add-card-button']").click()
    time.sleep(2)
    textArea= DRIVER.find_element(By.CSS_SELECTOR, value= "textarea[data-testid = 'list-card-composer-textarea']")
    textArea.clear()
    textArea.send_keys('Bot Added a Task')
    time.sleep(1)
    DRIVER.find_element(By.CSS_SELECTOR,value="button[data-testid = 'list-card-composer-add-card-button']").click()
    time.sleep(1)
    DRIVER.find_element(By.CSS_SELECTOR, value = "span[data-testid='CloseIcon']").click()
    time.sleep(2)
    
def takeScreenshot():
    date_str = date.today().strftime("%m-%d-%Y")
    fpath = os.path.join('downloads', f'{date_str}.png')
    DRIVER.get_screenshot_as_file(fpath)
    print("Screenshot is added to downloads folder!")
    
def main():
    try:
        DRIVER.get('https://trello.com')
        login()
        time.sleep(3)
        navigateToBoard()
        addTask()
        takeScreenshot()
        input("Bot operation Completed. Press any Key...")
        DRIVER.close()
    except Exception as e:
        print(e)
        DRIVER.close()


if __name__ == '__main__':
    main()
