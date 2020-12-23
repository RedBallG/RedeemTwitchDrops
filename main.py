from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
import random

def worker():
    chrome_options = webdriver.ChromeOptions()
    proxy = getProxies()
    chrome_options.add_argument('--proxy-server=%s' % proxy)
    #chrome_options.add_argument('headless')
    driver = webdriver.Chrome(options=chrome_options, executable_path='chromedriver.exe')
    driver.maximize_window()
    driver.get("https://twitch.tv/login")
    sleep(30)

    try:
        while(True):
            driver.get("https://www.twitch.tv/drops/inventory")
            sleep(20)
            try:
                #submit = driver.find_elements_by_class_name("tw-align-items-center tw-align-middle tw-border-bottom-left-radius-medium tw-border-bottom-right-radius-medium tw-border-top-left-radius-medium tw-border-top-right-radius-medium tw-core-button tw-core-button--overlay tw-core-button--primary tw-inline-flex tw-justify-content-center tw-overflow-hidden tw-relative")
                submit = driver.find_element_by_xpath("//button[@class='tw-align-items-center tw-align-middle tw-border-bottom-left-radius-medium tw-border-bottom-right-radius-medium tw-border-top-left-radius-medium tw-border-top-right-radius-medium tw-core-button tw-core-button--overlay tw-core-button--primary tw-inline-flex tw-justify-content-center tw-overflow-hidden tw-relative']")
                submit.click()
            except Exception as e:
                pass


    except Exception as e:
        print(e)
        sleep(3)


worker()