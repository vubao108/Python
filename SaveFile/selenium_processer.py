from selenium import  webdriver
from selenium.common.exceptions import *
import  logging
import  codecs
import SafariBook_Handle
import  requests
class Processor:
    def __init__(self, _driver):
        self.driver = _driver

    def click_menu(self, url):
        self.driver.get(url)
        try:
            menu_el = self.driver.find_element_by_tag_name("h1")
            try:
                menu_el.click()
                try:
                    self.driver.find_element_by_class_name("tocList")
                    return self.driver.page_source
                except NoSuchElementException:
                    logging.warn("not found tocList")
            except WebDriverException:
                logging.warn("menu_el not click able")
        except NoSuchElementException:
            logging.warn("not found menu_el")


        return None

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument(r"user-data-dir=D:\OtherProject\safariprofile")
    driver = webdriver.Chrome(chrome_options=options)
    driver.implicitly_wait(10)
    logging.basicConfig(filename="log_getMenu", level=logging.INFO, format="%(asctime)s : %(message)s")
    processor =  Processor(driver)
    menu_url = "https://www.safaribooksonline.com/library/view/expert-android-programming/9781786468956/a2dc1f24-f8d0-4d89-9f46-1e2cd0dc0a16.xhtml"
    html_content = processor.click_menu(menu_url)
    #print html_content
    #with codecs.open("demo_menu.html","w", encoding="utf-8") as f:
    #f.write(html_content)
    #print "ok"
    s = requests.Session()
    for cookie in driver.get_cookies():
        s.cookies.set(cookie['name'], cookie['value'])

    xuly = SafariBook_Handle.BookPage_Xuly(html_content, s)
    xuly.save_file(r"D:\OtherProject\SeleniumGetData\SaveFile\demo_menu2.html")
    print "ok"