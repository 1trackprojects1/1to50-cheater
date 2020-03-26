# copyright track projects 2020 aka @Track3CC or Track IC

import os
from selenium import webdriver
import selenium
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime

browser = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"))
browser.get('http://zzzscore.com/1to50/en/')

number = 1
while number != 51:
    print number
    buttons = browser.find_elements_by_xpath("//div[text()='" + str(number) + "']")
    for button in buttons:
        try:
            button.click()
        except selenium.common.exceptions.ElementNotInteractableException as error:
            pass
    number += 1
