# coding=utf-8

import selenium
from selenium import  webdriver
from bs4 import BeautifulSoup
import time
import base64
import json
import requests
import re
import SafariBook_Handle
import extra_tool
import logging
import codecs
import selenium_processer

if __name__ == "__main__":
    logging.basicConfig(filename="log_getBook",level=logging.INFO, format="%(asctime)s : %(message)s")
    tool = extra_tool.Tool()
    download_url = "https://www.safaribooksonline.com"
    options = webdriver.ChromeOptions()
    options.add_argument(r"user-data-dir=D:\OtherProject\safariprofile")
    driver = webdriver.Chrome(chrome_options=options)
    driver.implicitly_wait(10)


    driver.get(download_url)

    raw_input("login da nao")

    cookies = driver.get_cookies()
    s = requests.Session()
    for cookie in cookies:
        s.cookies.set(cookie['name'], cookie['value'])


    dir_to_save = "D:\\BooksSafari"
    count_page = 0
    with codecs.open("downloaded.txt","r",encoding="utf-8") as f:
        for line in f:
            if line.rstrip():
                download_url = line
                processor = selenium_processer.Processor(driver)
                html_content = processor.click_menu(download_url)
                if not html_content:
                    logging.warn("not able get menu link %s" % download_url)
                    continue

                safari_page_handle = SafariBook_Handle.BookPage_Xuly(html_content, s)
                title_page = safari_page_handle.get_title_page()
                file_path = tool.get_file_path(dir_to_save, download_url, 0, title_page)
                safari_page_handle.save_file(file_path)
                count_page +=1

                print "%d da download : %s" % (count_page, download_url)

    print "done"
    print "done"

