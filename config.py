import pathlib

USERNAME = ""   #Instagram account

PASSWORD = "" #Instagram password

DRIVER_EXECUTABLE_PATH = pathlib.Path(__file__).parent.absolute().joinpath("C:/Users/Rishi Patel/Documents/Git_demo/demos/Insta_Automation/chromedriver")

LIKE_XPATH = "//button//span//*[name()='svg' and @aria-label='Like']"

COMMENTBOX_PATH = "//div//form//*[name()='textarea' and @aria-label='Add a comment...']"

COMMENT_LIST = ['This is Great!','Amazing','WOW!','LOL','LMAO']

SAVE_XPATH = "//html//body//div[5]//div[2]//div//article//div[3]//section[1]//span[4]//div//div//button//div[1]//*[name()='svg' and @aria-label='Save']"

SKIP_LOGIN = False # skip log in flow. Useful if you have profile with cookies saved