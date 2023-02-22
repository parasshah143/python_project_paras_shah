from selenium import webdriver
import time


def launch_browser():
    d = webdriver.Chrome()
    d.get("http://google.com")
    print(d.title)
    time.sleep(10)
    d.quit()
