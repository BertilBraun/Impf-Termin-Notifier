import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys

mp = {
    # "12345": "AAAA-AAAA-AAAA", # TODO replace this
}

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


def crawl(key, plz, driver: WebDriver):
    url = "https://229-iz.impfterminservice.de/impftermine/suche/" + key + "/" + plz

    time.sleep(1)
    driver.get(url)
    time.sleep(1)

    try:
        driver.execute_script(
            "arguments[0].click();",
            driver.find_element_by_xpath(
                "/html/body/app-root/div/app-page-its-search/div/div/div[2]/div/div/div[5]/div/div[1]/div[2]/div[2]/button"
            ))
    except:
        print("Page not loaded!", url)
        return

    time.sleep(1)
    try:
        element = driver.find_element_by_xpath(
            "/html/body/app-root/div/app-page-its-search/app-its-search-slots-modal/div/div/div/div[2]/div/div/form/div[1]/span"
        )
        if not str(element.get_attribute("innerText")).strip().endswith("ob wieder Termine zur Verfügung stehen."):
            raise "Termin availible"
        print("element not found")
    except:
        driver.maximize_window()
        input("One was found!")


def main():
    driver = create()
    i = 0

    try:
        while True:
            print("Next Iteration:", i)
            i += 1
            for plz, key in mp.items():
                crawl(key, plz, driver)

            driver.get("https://www.google.com")
            time.sleep(180)

    except KeyboardInterrupt:
        print("Closing")
        driver.close()


if __name__ == "__main__":
    main()
