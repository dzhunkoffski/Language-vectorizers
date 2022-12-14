import os
from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

os.environ['PATH'] += r"C:/src/SeleniumChrome"
options = webdriver.ChromeOptions()
prefs = {"download.default_directory": "D:\\Downloads\\LibgenBooks"}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome('C:\\src\\SeleniumChrome\\chromedriver.exe', chrome_options=options)

total_links = 0

category_list = ['https://www.ebanglalibrary.com/category/%e0%a6%b8%e0%a7%87%e0%a6%ac%e0%a6%be-%e0%a6%aa%e0%a7%8d%e0%a6%b0%e0%a6%95%e0%a6%be%e0%a6%b6%e0%a6%a8%e0%a7%80/',
                 'https://www.ebanglalibrary.com/category/%e0%a6%ac%e0%a6%be%e0%a6%82%e0%a6%b2%e0%a6%be-%e0%a6%89%e0%a6%aa%e0%a6%a8%e0%a6%bf%e0%a6%b7%e0%a6%a6/',
                 'https://www.ebanglalibrary.com/category/%e0%a6%ac%e0%a6%be%e0%a6%82%e0%a6%b2%e0%a6%be-%e0%a6%b9%e0%a6%be%e0%a6%a6%e0%a6%bf%e0%a6%b8/',
                 'https://www.ebanglalibrary.com/category/%e0%a6%ac%e0%a6%be%e0%a6%82%e0%a6%b2%e0%a6%be-%e0%a6%ac%e0%a6%be%e0%a6%87%e0%a6%ac%e0%a7%87%e0%a6%b2/',
                 'https://www.ebanglalibrary.com/category/%e0%a6%ac%e0%a6%be%e0%a6%82%e0%a6%b2%e0%a6%be-%e0%a6%a4%e0%a7%8d%e0%a6%b0%e0%a6%bf%e0%a6%aa%e0%a6%bf%e0%a6%9f%e0%a6%95/',
                 'https://www.ebanglalibrary.com/category/%e0%a6%ac%e0%a6%be%e0%a6%82%e0%a6%b2%e0%a6%be-%e0%a6%b0%e0%a6%be%e0%a6%ae%e0%a6%be%e0%a7%9f%e0%a6%a3/',
                 'https://www.ebanglalibrary.com/category/%e0%a6%ac%e0%a6%be%e0%a6%82%e0%a6%b2%e0%a6%be-%e0%a6%aa%e0%a7%81%e0%a6%b0%e0%a6%be%e0%a6%a3/']

category_cnt = 0
for category_link in category_list:
    category_cnt += 1
    print("(", category_cnt, ")")

    driver.get(category_link)
    driver.implicitly_wait(20)
    driver.maximize_window()
    print("Now running category", category_cnt)

    with open('bangla_batch' + str(category_cnt) + '.txt', 'w', encoding='utf-8') as download_links:
        while True:
            driver.implicitly_wait(10)
            books = driver.find_element(by=By.CLASS_NAME, value='entries-wrap')
            book_list = books.find_elements(by=By.CLASS_NAME, value='entry-title-link')
            print("Total books on page", len(book_list))
            for book_link in book_list:
                total_links += 1
                download_links.write(book_link.get_attribute('href'))
                download_links.write('\n')
            try:
                next_space = driver.find_element(by=By.CLASS_NAME, value='pagination-next')
                next_button = next_space.find_element(by=By.TAG_NAME, value='a')
                next_button.click()
                time.sleep(1)
            except NoSuchElementException:
                print("Only one page!")
                break
    print("Already processed", total_links, "books")

print("Complete succesful! Total books found", total_links)
