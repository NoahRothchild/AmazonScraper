from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
from selenium.webdriver.common.by import By

def getAllDepts(webDriver):
	all_depts = webDriver.find_element_by_id("zg_browseRoot")
	dept_list = all_depts.find_elements_by_tag_name("li")
	a_list = list()
	href_list = list()
	for el in dept_list:
		try:
			a_list.append(el.find_element_by_tag_name("a"))
		except:
			pass
	for href in a_list:
		href_list.append(href.get_attribute('href'))
	return href_list

def getDeptProducts(href, webDriver):
	webDriver.get(href)
	allProductHrefs = list()
	rawHrefs = list()
	
	containers = webDriver.find_elements_by_tag_name('img')
	rawProducts = webDriver.find_elements_by_class_name('a-link-normal')

	for product in rawProducts:
		rawHrefs.append(product.get_attribute('href'))
		print(product.get_attribute('href'))
	for c in containers:
		print(c.get_attribute('alt'))
		try:
			print(c.get_attribute('alt'))
		except:
			pass
	allProductHrefs.append(rawHrefs)
	time.sleep(random.randint(1,20))
	for href in rawHrefs:
		if 'product-reviews' not in str(href):
			webDriver.get(href)
			break
	time.sleep(random.randint(1,20))
	rawHrefs.clear()

	# outputDeptToFile(dept_name, products)
def getProduct(href, webDriver):
	webDriver.get(href)

def outputDeptToFile(dept, products):
	print('asf')

def driver():
	webDriver = webdriver.Chrome()
	webDriver.get("https://www.amazon.com/best-sellers/zgbs")
	hrefs = getAllDepts(webDriver)
	for href in hrefs:
		getDeptProducts(href, webDriver)
	webDriver.close()

if __name__ == '__main__':
	driver()



'''
GET ALL DEPTS
'CLICK' ON EACH
GET ALL SUB DEPT - optional for now
SCRAPE ALL PRODUCT NAMES 
OUTPUT THEM TO A FILE 
''' 
