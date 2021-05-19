import time
from util import *

# TODO enter the plz of the stations you want to monitor
plzs = [
    "70174",
    "72072",
    "72213",
    "71065",
    "70629"
]


def crawl(plz, driver):
    url = "https://229-iz.impfterminservice.de/impftermine/service?plz=" + plz

    driver.get(url)
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
            onSuccess(url)
        except:
            print("element not found")


def main():
    driver = create()

    try:
        for i in range(500):
            print("Next Iteration:", i)
            for plz in plzs:
                crawl(plz, driver)

            driver.get("https://www.google.com")
            time.sleep(180)

    except KeyboardInterrupt:
        destroy(driver)


if __name__ == "__main__":
    main()
