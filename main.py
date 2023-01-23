import time
import json
import os.path
from selenium import webdriver
# import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from selenium. webdriver.common.desired_capabilities import DesiredCapabilities
def handler(event=None, context=None):
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.binary_location = "/opt/chrome/chrome"
    driver_path='/usr/bin/chromedriver'
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("--disable-dev-shm-usage")
    # chrome_options.add_argument("--disable-gpu")
    # chrome_options.add_argument("--disable-dev-tools")
    # chrome_options.add_argument("--no-zygote")
    # chrome_options.add_argument("--single-process")
    # chrome_options.add_argument("window-size=2560x1440")
    # chrome_options.add_argument("--user-data-dir=/tmp/chrome-user-data")
    # chrome_options.add_argument("--remote-debugging-port=9222")
    #chrome_options.add_argument("--data-path=/tmp/chrome-user-data")
    #chrome_options.add_argument("--disk-cache-dir=/tmp/chrome-user-data")
    driver=webdriver.Chrome(driver_path)
    # driver=webdriver.Remote('http://localhost:4445',desired_capabilities=DesiredCapabilities.CHROME)
    # driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://python.org")
    driver.save_screenshot('C:\\Users\\yashs\\Desktop\\Lambdawithselenium\\dockerandlambda\\app\\screenshot3.png')
    # print(driver.current_url)

handler()