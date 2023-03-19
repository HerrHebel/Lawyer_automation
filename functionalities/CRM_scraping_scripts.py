from dotenv import load_dotenv
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import time

load_dotenv("env_var/.env")
username = os.getenv("CRM_USERNAME")
password = os.getenv("CRM_PASSWORD")
case_url = os.getenv("CASE_URL")


def selenium_setup():
    """
    Setting up and defining webdriver used to perform scraping operations.
    :return: class 'selenium.webdriver.chrome.webdriver.WebDriver', webdriver object
    """
    path_to_chrome_web_driver = os.path.dirname(
        __file__) + 'webdriver/chromedriver/chromedriver'
    chrome_webdriver_service = Service(executable_path=path_to_chrome_web_driver)
    options = Options()
    options.page_load_strategy = "normal"
    driver = webdriver.Chrome(service=chrome_webdriver_service, options=options)
    return driver


def crm_client_data_scrape(context):
    """
    The function scrapes client address data from CRM webpage.
    :param context: dict, Set of data to be used in docx document creation the function is going to write the output to.
    :return: dict, input dict with WSA address data saved into it
    """
    driver = selenium_setup()
    case_id = context["crm_case_number"]
    # Login process
    driver.get(f"{case_url}{case_id}")
    crm_username_box = driver.find_element(By.XPATH, '//*[@id="loginform-username"]')
    crm_password_box = driver.find_element(By.XPATH, '//*[@id="loginform-password"]')
    crm_login_submit_button = driver.find_element(By.XPATH, '//*[@id="login-form"]/div[2]/button')
    crm_username_box.send_keys(username)
    crm_password_box.send_keys(password)
    crm_login_submit_button.click()
    time.sleep(1)
    # Data scraping
    driver.find_element(By.XPATH, '//*[@id="issue-details"]/div/div[1]/div[1]/fieldset[1]/legend/a').click()
    time.sleep(1)
    try:
        client_name_scrape = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div/div/div/h1').text
        client_street_scrape = driver.find_element(By.XPATH, '//*[@id="w1"]/tbody/tr[5]/td').text
        client_city_scrape = driver.find_element(By.XPATH, '//*[@id="w1"]/tbody/tr[4]/td').text
        # Data cleaning
        client_surname_name = client_name_scrape
        client_street = client_street_scrape
        client_zip_city = f"{client_city_scrape.split(' - ')[1][1:-1]} {client_city_scrape.split(' - ')[0]}"
    except NoSuchElementException:
        print(f"Scraping script failed. Selenium was no able to find appropriate element on CRM website. Please "
              f"review the file for case no. {context['crm_case_number']}")
        client_surname_name = f"Failed scrape attempt case number {context['crm_case_number']}"
        client_street = "Enter data manually"
        client_zip_city = "Enter data manually"
    # Saving data to context
    context["client_surname_name"] = client_surname_name
    context["client_street_name_number"] = client_street
    context["client_zip_city"] = client_zip_city
    return context
    driver.quit()