import time
import pandas as pd
from pandas.core.arrays.categorical import contains
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

import requests
import os

from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def zara_website(url):
    chrome_options = Options()
    # chrome_options.add_argument("--headless")

    executable_path = ChromeDriverManager().install()
    service = Service(executable_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(url)

    login = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'LOG IN')]"))
        )
    #login.click()

    help_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Help')]"))
    )
    help_button.click()

    categories_container = driver.find_element(By.CLASS_NAME, "help-center-categories-std__container")

    titles = categories_container.find_elements(By.TAG_NAME, "h3")
    print(titles)
    # prolayim po listu

    for h3 in titles:
        print(h3.text)

    elements = driver.find_elements(By.XPATH, "//*[@data-qa-id='article-link']")
    for element in elements:
        print(element.text)





        #ladfla kflkhsdg hlzhksfd glih














    time.sleep(123)
    return login


if __name__ == '__main__':

    zara_url="https://www.zara.com/rs/en/"
    dr = zara_website(url = zara_url)
    print(1)




r"C:\Users\User\Downloads\chromedriver"


# {element}.get_attribute("innerHTML")
#login_elements = driver.find_elements(By.XPATH, "//span[contains(text(),'LOG IN')]")


# time.sleep(15)
# login = driver.find_element(By.XPATH, "//span[contains(text(),'LOG IN')]")
# login.click()


########################################################################################

# # Locate the parent <ul> element with class "listH"
# categories_list = driver.find_element(By.CLASS_NAME, "listH")
#
# # Find all <li> elements within the <ul class="listH">
# li_elements = categories_list.find_elements(By.TAG_NAME, "li")
#
# # Iterate through each <li> and extract links (text and href)
# for li in li_elements:
#     # Find the <a> element inside the <li>
#     a_elements = li.find_elements(By.TAG_NAME, "a")
#
#     for a in a_elements:
#         # Extract the text and the href attribute of each <a> link
#         link_text = a.text
#         link_url = a.get_attribute("href")
#
#         print(f"Link Text: {link_text}, Link URL: {link_url}")