from selenium import webdriver
import time
if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    print 'minimize'
    driver.minimize_window()
    time.sleep(5)
    driver.maximize_window()