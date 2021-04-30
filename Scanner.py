import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys

# TODO enter the plz of the stations you want to monitor
plzs = [
    "70174",
    "72072",
    "72213",
    "71065"
]

print("\nStarting...\n")


def create():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.binary_location = r"D:\Program Files\Google\Chrome\Application\chrome.exe"
    # options.add_argument("--disable-gpu")
    # options.add_argument("--headless")

    driver = webdriver.Chrome(
        executable_path=r"C:\Users\Bertil\OneDrive\Desktop\Impf Termin Notifier\chromedriver.exe", options=options)

    driver.minimize_window()

    return driver


def crawl(plz, driver: WebDriver):
    driver.get(
        "https://229-iz.impfterminservice.de/impftermine/service?plz=" + plz)
    time.sleep(2)

    try:
        driver.find_element_by_xpath("/html/body/section/div[2]/div/div/h1")
    except:
        driver.execute_script(
            "arguments[0].click();",
            driver.find_element_by_xpath(
                "/html/body/app-root/div/app-page-its-login/div/div/div[2]/app-its-login-user/div/div/app-corona-vaccination/div[2]/div/div/label[2]/input"
            ))

        time.sleep(5)
        try:
            driver.find_element_by_xpath(
                "/html/body/app-root/div/app-page-its-login/div/div/div[2]/app-its-login-user/div/div/app-corona-vaccination/div[3]/div/div/div/div[2]/div/app-corona-vaccination-no/div[1]"
            )
            driver.maximize_window()
            input("One was found!")
        except:
            print("element not found")


def main():
    driver = create()
    i = 0

    try:
        while True:
            print("Next Iteration:", i)
            i += 1
            for plz in plzs:
                crawl(plz, driver)

            driver.get("https://www.google.com")
            time.sleep(180)

    except Exception as e:
        print("Closing because of:", e)
        driver.close()


if __name__ == "__main__":
    main()
