import os
from selenium import webdriver

print("\nStarting...\n")


def onSuccess(url):
    os.startfile(url)
    input("One was found!")


def create():
    options = webdriver.ChromeOptions()
    options.binary_location = r"D:\Program Files\Google\Chrome\Application\chrome.exe"
    options.add_argument("--incognito")
    driver = webdriver.Chrome("chromedriver.exe", options=options)

    driver.minimize_window()

    return driver


def destroy(driver):
    print("Closing")
    driver.quit()
