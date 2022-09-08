import os
import string

from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up
os.environ['PATH'] += r"C:/src/SeleniumChrome"
options = webdriver.ChromeOptions()
prefs = {"download.default_directory": "D:\\Downloads\\LibgenBooks"}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome('C:\\src\\SeleniumChrome\\chromedriver.exe', chrome_options=options)
BATCH_NO = 8
startFrom = 0

# Based on BATCH_NO variable
links_file = "bangla_batch" + str(BATCH_NO) + ".txt"
write_to = "D:\\BBooks\\batch" + str(BATCH_NO) + "\\"

link_cnt = startFrom
text_cnt = 0
with open(links_file, 'r', encoding='utf-8') as download_links:
    links = download_links.readlines()
    for i in range(startFrom, len(links)):

        print(link_cnt, '/', len(links), ':', links[i])
        link_cnt += 1
        driver.get(links[i])
        driver.maximize_window()
        time.sleep(0.5)

        try:
            book = driver.find_element(by=By.XPATH, value='//*[@id="genesis-content"]/article/div/div[1]')
        except:
            print("Error !!!")
            continue
        paragraphs = book.find_elements(by=By.TAG_NAME, value='p')

        # Get actual bookname
        bread_crumb = driver.find_element(by=By.XPATH, value='//*[@id="top"]/div[2]/div[1]')
        numberOfCrumbs = (len(bread_crumb.find_elements(by=By.TAG_NAME, value='span')) - 1) // 2 + 1
        print(numberOfCrumbs, bread_crumb.get_attribute('class'))

        book_name = driver.find_element(
            by=By.XPATH, value='//*[@id="top"]/div[2]/div[1]/span[' + str(numberOfCrumbs - 1) + ']/a/span'
        ).get_attribute('innerHTML').translate(str.maketrans({key: '-' for key in string.punctuation + '\t'}))

        # Get actual chaptername
        chapter_name = driver.find_element(
            by=By.XPATH, value='//*[@id="top"]/div[2]/div[1]/span[' + str(numberOfCrumbs) + ']'
        ).get_attribute('innerHTML').translate(str.maketrans({key: '-' for key in string.punctuation + '\t'}))
        print(book_name)
        print(chapter_name)

        # Change filenames
        try:
            with open(write_to + book_name + '_' + chapter_name + '.txt', 'w', encoding='utf-8') as book_text:
                for paragraph in paragraphs:
                    book_text.write(paragraph.text)
                    book_text.write('\n')
        except:
            with open(write_to + book_name + '_' + chapter_name[0] + '.txt', 'w', encoding='utf-8') as book_text:
                for paragraph in paragraphs:
                    book_text.write(paragraph.text)
                    book_text.write('\n')
