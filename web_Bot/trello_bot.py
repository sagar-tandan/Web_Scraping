from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
from datetime import date
import os
import json

service = Service(executable_path='chromedriver.exe')
DRIVER = webdriver.Chrome(service=service)
        
def main():
    try:
        DRIVER.get('https://trello.com')
        input("Bot operation Completed. Press any Key...")
        DRIVER.close()
    except Exception as e:
        print(e)
        DRIVER.close()


if __name__ == '__main__':
    main()
