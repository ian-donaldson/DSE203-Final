import time
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

import pandas as pd

page_url = "https://siccode.com/"


driver = webdriver.Chrome('./chromedriver')


delay = 3 # seconds
company_list = ["Alibaba", "Microsoft", "Ebay"]
naics_list = []
try:
    for company in company_list:
        driver.get(page_url)
        searchBox = driver.find_element_by_id("keyword_m")
        searchBox.send_keys(company)
        driver.find_element_by_xpath("/html/body/div[1]/article/section[1]/div/form/div/div[2]/input").click()
        
        try:
            #this is the block if the naics code exists upon initial search
            company_code = driver.find_element_by_xpath("//*[@id='result-naics']/ul/li/a/div").text
            naics_code_page = driver.find_element_by_xpath("//*[@id='result-naics']/ul/li/a").click()
        except:
            print('naics does not exist')
            #wait for element to load
            myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'result-top-companies')))
            first_company = driver.find_element_by_xpath("//*[@id='result-top-companies']/ul/li[1]/a").click()

            company_code = driver.find_element_by_xpath("//*[@id='description']/div[2]/div/div/a[2]/span").text.split("NAICS CODE ")[1]
            naics_code_page_href = driver.find_element_by_css_selector(".detail-summary .naics").get_attribute('href')
            driver.get(naics_code_page_href)


        #we want to go a few levels deep, one iteration per naics code stripped
        for i in range(5):
            #get the title
            naics_title = driver.find_element_by_xpath("//*[@id='main']/div/h1").text.split("- ")[1]
            #add to our list of tuples
            naics_list.append((company, company_code, naics_title))
            #find the parent of the naics stripped
            company_code = driver.find_element_by_xpath("//*[@id='hierarchy']/div/div/div[2]/div/div[1]/ul/li[1]/a/span[1]").text
            #chose to use css selector because xpath errored here for me
            href_of_parent = driver.find_element_by_css_selector(".hierarchy-list a").get_attribute('href')
            #move on to next page please note that I use href rather than clicking because 
            #clicking often times there's an error that can't click on element because of AD. 
            #also .get waits for everything to load
            driver.get(href_of_parent)
        time.sleep(2)
finally:
    print('final naics', naics_list)
    driver.close()
    df = pd.DataFrame(naics_list, columns =['Company', 'NAICS_CODE', 'NAICS_TITLE'])
    df.to_csv("naics_scraped.csv")
