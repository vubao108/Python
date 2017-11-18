#^- coding: utf-8 -^-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
import  time
import codecs
loginUrl = "http://daotaogdbhyt.baohiemxahoi.gov.vn/Account/Index"
getUrl = "http://daotaogdbhyt.baohiemxahoi.gov.vn/DM_GOITHAUCHITIET/Index/"
url_list = [4976,4977,1833,1832,4995]
#4975,1852,


def find_nextpage_el(driver):
    try:
        nextpage = driver.find_element_by_xpath("//div[@id='gvEditing_DXPagerBottom']//img[@class='dxWeb_pNext_EIS' and @src='/DXR.axd?r=1_36-FCJQe']")
        return nextpage
    except NoSuchElementException:
        return ''

def wait_text_appear(driver, el):
    driver.execute_script("arguments[0].scrollIntoView()",el)
    break_count = 0
    while break_count < 20:
        if len(el.text) > 0:
            print "break_count %d" % (break_count)
            return el.text
        else:
            break_count = break_count + 1
            time.sleep(0.5)
    print "break_count %d"%(break_count)
    return ""

if __name__ == '__main__':
    driver = webdriver.Chrome()
    #driver = webdriver.Firefox()
    #driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(loginUrl)
    raw_input("enter to continue")

    index = 0
    for i in url_list:
        index = index + 1
        print str(index) + "---------" + str(i)
        filedata = 'D:\\Work\\bhxh_' + str(i) + ".txt"
        data_file = codecs.open(filename=filedata, encoding='utf-8', mode='w')
        driver.get(getUrl + str(i))


       # body = driver.find_element_by_tag_name("body")


        #for i in range(0,3):
        #nextpage_demo = find_nextpage_el(driver)
        if index == 1:
            #raw_input("minimie window to continue")
            driver.minimize_window()
            time.sleep(5)
            driver.maximize_window()
        #driver.set_window_size(0,0)
        #time.sleep(2)
        #driver.maximize_window()
        while True:
            try:
                el_row = driver.find_element_by_xpath("//tr[@id='gvEditing_DXDataRow0']")
                break
            except NoSuchElementException:
                print "error at : %d "%(index)
                print "relogin to continue: "
                driver.get(loginUrl)
                raw_input (" minimize chrome and enter to continue")


        for row in range(0,10):
            #current_row = driver.find_element_by_xpath("//tr[@id='gvEditing_DXDataRow%d']"%(row))
            for i in range(1,27):
                try:
                    el_td = driver.find_element_by_xpath("//tr[@id='gvEditing_DXDataRow%d']/td[%d]"%(row,i))
                    tmp = ""
                    if i != 4 and i != 12 and i != 26:
                        tmp = wait_text_appear(driver, el_td)


                    print   "%d %d  %s" %(row, i, tmp)
                    data_file.write(tmp + "|" )
                except NoSuchElementException:
                    break

            data_file.write("\n")

        row_num = 10
        not_break_flag = True
        while True and  not_break_flag:
            nextpage_el = find_nextpage_el(driver)
            if nextpage_el == '':
                break
            try:
                nextpage_el.click()

                for row in range(row_num, row_num + 10):
                    #current_row = driver.find_element_by_xpath("//tr[@id='gvEditing_DXDataRow%d']" % (row))
                    for i in range(1, 27):
                        try:
                            el_td = driver.find_element_by_xpath("//tr[@id='gvEditing_DXDataRow%d']/td[%d]"%(row,i));
                            tmp = ""
                            if i != 4 and i != 12 and i != 26:
                                tmp = wait_text_appear(driver, el_td)


                            print   "%d %d  %s" % (row, i, tmp)
                            data_file.write(tmp + "|")
                        except NoSuchElementException:
                            print 'not found el_td'
                            not_break_flag = False
                            break

                    data_file.write("\n")
                    if not not_break_flag :
                        break
                row_num = row_num + 10
            except WebDriverException:
                print 'nextpage not clickable'
                break

        data_file.close()



    print "OK"
    #driver.execute_script("window.scrollBy(500,0);")

