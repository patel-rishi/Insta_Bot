import time, config, random
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import ui

class AutoLikeBot():
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def wait_until(self, condition, timeout=5):
        WebDriverWait(self.driver, timeout).until(condition)
    
    def log_in(self):
        try:
            self.wait_until(EC.presence_of_element_located((By.NAME, 'username')))

            try:
                self.driver.find_element_by_name('username').send_keys(config.USERNAME)
                self.driver.find_element_by_name('password').send_keys(config.PASSWORD)
                self.driver.find_element_by_name('password').send_keys(Keys.RETURN)

            except NoSuchElementException as e:
                print(f"Could not find element. Error: {e}")
                return

        except TimeoutException:
            pass
        
        time.sleep(3)
        try:
            self.driver.find_element_by_xpath('//*[text() = "Not Now"]').click()
        except TimeoutException or NoSuchElementException as e:
            print(f"Could not find element. Error: {e}")
            return
        
        time.sleep(5)
        try:
            # turn on notifications prompt
            self.driver.find_element_by_xpath('//*[text() = "Not Now"]').click()
            print("Skipping turn on notifications")
        except NoSuchElementException as e:
            print(f"Could not find element. Error: {e}")
            return

    def navigate_explore(self):
        self.driver.get("https://www.instagram.com/explore/")

        #Wait for page to load
        self.driver.set_page_load_timeout(5)
        self.driver.implicitly_wait(2)

        try:
            first_post = self.driver.find_element_by_tag_name("a").click()
            self.driver.set_page_load_timeout(5)
            time.sleep(2)
        except TimeoutException:
            pass

    def like_post(self):
        like_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "config.LIKE_XPATH"))).click()
        time.sleep(2)

    def comment(self):
        rand = [0,1]
        if random.choice(rand) == 1:
            commentArea = self.driver.find_element_by_class_name('Ypffh')
            commentArea.click()
            time.sleep(2)
            commentArea = self.driver.find_element_by_class_name('Ypffh')
            commentArea.click()
            commentArea.send_keys(random.choice(config.COMMENT_LIST))
            commentArea.send_keys(Keys.RETURN)

    def save_and_next(self):
        # Not solved
        #save_post = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "config.SAVE_XPATH"))).click()
        time.sleep(2)
        next_post = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Next"))).click()

    def operations(self):
        self.log_in()
        self.navigate_explore()
        i = 5
        while i > 0:
            self.like_post()
            self.comment()
            self.save_and_next()
            i = i - 1

