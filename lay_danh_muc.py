#^-coding: utf-8 -^-
from selenium import webdriver
import logging
from selenium.common.exceptions import *
import time
import  datetime

# return list of dictionary info 
def get_danh_muc(driver):
	result_list = []
	danh_muc_url = 'http://daotaogdbhyt.baohiemxahoi.gov.vn/DM_GOITHAU'
	tim_button_xpath = "//img[@id='bt_TimKiemImg']"
	next_xpath = "//div[@id='gvGoiThau_DXPagerBottom']//img[@class='dxWeb_pNext_EIS' and @src='/DXR.axd?r=1_36-FCJQe']" 
	
	driver.get(danh_muc_url)
	raw_input("login nao:")
	driver.get(danh_muc_url)
	
	try:
		tim_button = driver.find_element_by_xpath(tim_button_xpath)
		try:
			tim_button.click()
			logging.info("tim_button clicked")
			time.sleep(5)
		except WebDriverException:
			logging.warning("tim_button not clickable")
			return -1
	except NoSuchElementException:
		logging.warning("not found tim_button")
		return -1
		
		
	get_data_in_page(driver, result_list)
	
		
	while True:
		try:
			next_page_button = driver.find_element_by_xpath(next_xpath)
			try:
				next_page_button.click()
				get_data_in_page(driver, result_list)
			except WebDriverException:
				logging.warning("next_page_button not clickable")
				break
		except NoSuchElementException:
			logging.warning("Not found next_page_button")
			break
	
	
	
	return result_list
	
def get_data_in_page(driver, total_list):
	
	list_row_xpath = "//table[@id='gvGoiThau_DXMainTable']//tr[contains(@id,'gvGoiThau_DXDataRow')]"
	data_col_xpath = "./td"
	list_row = driver.find_elements_by_xpath(list_row_xpath)
	
	logging.info("number of data row: %d", len(list_row) )
	for index in range(0, len(list_row)):
		row = list_row[index]
		list_data_col = row.find_elements_by_xpath(data_col_xpath)
		url_index = list_data_col[9].find_element_by_xpath("./a").get_attribute("href")[25:]
		data_dict = {"stt":list_data_col[0].text,
					"so_qd":list_data_col[1].text,
					"nam":list_data_col[2].text,
					"ngay_cong_bo":list_data_col[3].text,
					"ngay_het_han":list_data_col[4].text,
					"loai":list_data_col[5].text,
					"tong":list_data_col[6].text,
					"hieu_luc":list_data_col[7].text,
					"trang_thai":list_data_col[8].text,
					"url_index":url_index
					}
		logging.info("%d %s", index, data_dict)
		total_list.append(data_dict)

if __name__ == "__main__":
	logfile = "log_laydanhmuc_%s"%datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
	logging.basicConfig(filename=logfile,level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s' )
	driver = webdriver.Chrome()
	#driver = webdriver.Firefox(
	#driver.maximize_window()
	driver.implicitly_wait(10)
	tong_so_danh_muc = get_danh_muc(driver)
	print tong_so_danh_muc
	raw_input("enter to close Chrome")
	driver.quit()
	
		
		
	
	