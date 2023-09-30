from tkinter import messagebox
import requests
import selenium.webdriver
from selenium.webdriver.chrome.options import Options
import os
import webbrowser
from sys import exit
import traceback




class Fun:

    def Fupdate():
        myv = "1.0.1"
        linkrep = requests.get("https://outide.6te.net/Servers.html")
        nvr = linkrep.text
        if(myv!=nvr):
            chl = requests.get("https://pastebin.com/raw/URWKx7fp")
            log = chl.text
            reply = (messagebox.showinfo("Update","New Update is Released , Download "+log))
            if(reply=="ok"):
                webbrowser.open('https://outide.6te.net/cookini.zip')
            exit()

    def onClick():
        messagebox.showinfo("Hello","Codded By Dhia")
        webbrowser.open('https://www.facebook.com/dh.bejaoui')
        __class__.Netflix()


    def __downloadDn():
        linkrep = requests.get("https://outide.6te.net/bacflix.php")
        link = linkrep.text
        print(link)
        response = requests.get(link)
        data = response.text
        fh = open("config.dat","w")
        for line in data.splitlines():
            line = line.replace("true","True")
            line = line.replace("false","False")
            if(line.find("sameSite")!=-1):
                continue
            if(line.find("null")!=-1):
                continue
            fh.write(line+"\n")
        
        fh.close()
        fh = open("config.dat","r")
        data=fh.read()
        fh.close()
        os.remove("config.dat")
        data = eval(data)
        return (data , link)

    def Netflix():
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = selenium.webdriver.Chrome(options=chrome_options)
        driver.get("https://www.netflix.com/")
        try:
            data,link = __class__.__downloadDn()
        except Exception as e:
            requests.get("https://outide.6te.net/bacflix.php?url="+link)
            driver. close()
            __class__.Netflix()
        cookies = list(data)
        try:
            for cookie in cookies:
                driver.add_cookie(cookie)
        except:
            pass
        driver.get("https://www.netflix.com/browse")
        try:
            driver.execute_script("document.getElementsByClassName('profile-gate-label')[0].childNodes[0].textContent = 'Codded By Dhia'")
            driver.execute_script("window.open('https://www.netflix.com/tv9',' _blank');")

        except:
            get_url = driver.current_url
            if(get_url.find("nextpage")!=-1):
                requests.get("https://outide.6te.net/bacflix.php?url="+link)
                driver. close()
                __class__.Netflix()
            else:
                driver.execute_script("window.open('https://www.netflix.com/tv9',' _blank');")