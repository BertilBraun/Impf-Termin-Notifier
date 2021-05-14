import time
from util import *

mp = {
    # "12345": "AAAA-AAAA-AAAA", # TODO replace this
}


def crawl(key, plz, driver):
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
        onSuccess(url)


def main():
    driver = create()

    try:
        for i in range(500):
            print("Next Iteration:", i)
            
            for plz, key in mp.items():
                crawl(key, plz, driver)

            driver.get("https://www.google.com")
            time.sleep(180)

    except KeyboardInterrupt:
        destroy(driver)


if __name__ == "__main__":
    main()
