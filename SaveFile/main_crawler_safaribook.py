import pyvirtualdisplay
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

if __name__ == "__main__":
    logging.basicConfig(filename="log_getBook",level=logging.INFO)
    tool = extra_tool.Tool()
    root_url = 'https://www.google.com'
    download_url1 = 'https://www.safaribooksonline.com'
    download_url='https://www.safaribooksonline.com/library/view/automate-the-boring/9781457189906/ch12.html'
    start_page_url = 'https://www.safaribooksonline.com/library/view/automate-the-boring/9781457189906/cover.html'
    #current_url = 'https://www.safaribooksonline.com/library/view/automate-the-boring/9781457189906/ch11.html'
    #driver = webdriver.Chrome()
    options = webdriver.ChromeOptions()
    options.add_argument(r"user-data-dir=D:\OtherProject\safariprofile")
    driver = webdriver.Chrome(chrome_options=options)



    driver.get(download_url)

    current_url = raw_input(" enter url: \n:")
    current_url = current_url.rstrip()
    count_page = raw_input(" bat dau tu page 1,2,3,... : ")
    count_page = int(count_page.rstrip())

    cookies = driver.get_cookies()
    s = requests.Session()
    for cookie in cookies:
        s.cookies.set(cookie['name'], cookie['value'])

    '''
    response = s.get(download_url, stream = True)
    newfilepath = "safari01.html"
    filedata = file(newfilepath,"wb")
    for block in response.iter_content(1024):
        if not block:
            break
        filedata.write(block)
    '''
    dir_to_save = "D:\\BooksSafari\\PythonDownload"

    download_url = current_url
    print "start"
    while True:


        #s.encoding = 'utf-8'
        response = s.get(download_url)

        html_content = response.text
        safari_page_handle = SafariBook_Handle.BookPage_Xuly(html_content, s)
        title_page = safari_page_handle.get_title_page()
        file_path = tool.get_file_path(dir_to_save, download_url, count_page, title_page)
        safari_page_handle.save_file(file_path)
        print "%d da download : %s" %(count_page,download_url)

        download_url = safari_page_handle.get_next_page_link()
        count_page += 1
        if not download_url:
            break




    #for css_item in parser.find_all("link",{"rel":"stylesheet"}):




    print "done"