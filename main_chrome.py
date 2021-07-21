import selenium, time, config, pathlib
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bot import AutoLikeBot


def configure_chrome_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')

    driver = webdriver.Chrome(executable_path=config.DRIVER_EXECUTABLE_PATH, options=options)
    driver.maximize_window()
    driver.get("https://www.instagram.com")
    # page loading time and wait time for page reload
    driver.set_page_load_timeout(5)
    driver.implicitly_wait(2)
    return driver

if __name__ == "__main__":
    configure_chrome_driver()
    # AutoLikeBot.operations()
    ovar = AutoLikeBot(configure_chrome_driver())
    ovar.operations()



