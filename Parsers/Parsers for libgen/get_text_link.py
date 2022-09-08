import os
from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Selenium
os.environ['PATH'] += r"C:/SeleniumDrivers"
options = webdriver.ChromeOptions()
prefs = {"download.default_directory": "D:\\Downloads\\LibgenBooks"}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome('C:\\SeleniumDrivers\\chromedriver.exe', chrome_options=options)

# Search parameters
value = 'chinese'
search_in_fields = 'language'
view_results = 'simple'
extensions = {'epub', 'txt', 'fb2', 'mobi'}

with open('libgen_links.txt', 'w') as download_links:
    for page in range(1, 100):
        driver.get('http://libgen.is/search.php?&res=100&req='+value+'&phrase=1&view='+view_results+'&column='+search_in_fields+'&sort=def&sortmode=ASC&page='+str(page))
        driver.implicitly_wait(20)
        driver.maximize_window()

        for row in range(2, 101):
            extension = driver.find_element_by_xpath('./html/body/table[3]/tbody/tr[' + str(row) + ']/td[9]').get_attribute('innerHTML')
            if (extension in extensions):
                link = driver.find_element_by_xpath('./html/body/table[3]/tbody/tr[' + str(row) + ']/td[10]/a')
                download_links.write(link.get_attribute('href'))
                download_links.write('\n')