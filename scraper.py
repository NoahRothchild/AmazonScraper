from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
from selenium.webdriver.common.by import By

import mysql.connector
from mysql.connector import errorcode

def connect_db():
    try:
        cnx = mysql.connector.connect(user='admin', password='password', host='52.14.225.18', port='3306', database='CloverdaleCapital')
        cursor = cnx.cursor()

        add_product = ('INSERT INTO Product '
                        '(Name, PID, Made_by) '
                        'VALUES (%s, %s, %s)')
        data_product = ('Name of product', 'PID Number', 'Made by company')

        cursor.execute(add_product, data_product)

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('User/pass error')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print('DB does not exist')
        else:
            print(err)
    else:
        cnx.commit()
        cursor.close()
        cnx.close()

#currently skipping audio books, collectible currencies

def getAllDepts(webDriver, Cat_list, href_list):
	all_depts = webDriver.find_element_by_id("zg_browseRoot")
	dept_list = all_depts.find_elements_by_tag_name("li")
	a_list = list()
	# href_list = list()
	for el in dept_list:
		try:
			a_list.append(el.find_element_by_tag_name("a"))
		except:
			pass
	for href in a_list:
		href_list.append(href.get_attribute('href'))
		Cat_list.append(href.get_attribute('innerHTML'))
	# return href_list
	return

def getDeptProducts(href, dept, webDriver):
	webDriver.get(href)
	allProductHrefs = list()
	rawHrefs = list()
	
	containers = webDriver.find_elements_by_tag_name('img')
	# rawProducts = webDriver.find_elements_by_class_name('zg-ordered-list > li > span > div > span > a')

	rawProducts = list()
	
	for x in range(1,53):
		try:
			y = '#zg-ordered-list > li:nth-child(%s) > span > div > span > a'%(x)
			data = webDriver.find_element_by_css_selector(y)
			rawHrefs.append(data.get_attribute('href'))
			print(data.get_attribute('href'))	
		except:
			pass
	for product in range(len(rawProducts)):
		print(rawProducts[product])
	# for c in containers:
	# 	print(c.get_attribute('alt'))
	# 	try:	
	# 		pass
	# 		print(c.get_attribute('alt'))
	# 	except:
	# 		pass
	# time.sleep(500)
	allProductHrefs.append(rawHrefs)
	time.sleep(random.randint(1,20))
	counter = 0
	for href in rawHrefs:
		if(dept == "Audible Books &amp; Originals" or dept == "Books" or dept == "CDs &amp; Vinyl"or dept == "Collectible Currencies" or dept == "Digital Music" or dept == "Entertainment Collectibles" or dept == "Gift Cards" or dept == "Kindle Store" or dept == "Magazine Subscriptions" or dept == "Movies &amp; TV"):
			break
		if counter < 50:
			brand = ""
			if 'product-reviews' not in str(href):
				if 'new-releases' not in str(href):
					if 'movers-and-shakers' not in str(href):
						if 'Appstore-Android' not in str(href):
							if 'most-wished-for' not in str(href):
								counter = counter + 1
								print(counter)
								webDriver.get(href)
								getBrand(brand, href, dept, webDriver)	
	time.sleep(random.randint(1,20))
	rawHrefs.clear()

def getBrand(brand, href, dept, webDriver):
	
	productName = ""
	if(dept == "Apps &amp; Games"):
		data = webDriver.find_element_by_id('brand')
		brand = data.get_attribute('innerHTML').strip()
		print(brand)
		productName = webDriver.find_element_by_css_selector("div#mas-title > div > span").get_attribute('innerHTML').strip()

	else:
		try:
			data = webDriver.find_element_by_css_selector('a#bylineInfo')
			brand = data.get_attribute('innerHTML').strip()
			if(brand[:2] == "by" and (brand[3] == "\n" or brand[3] == " " or brand[3] == "\t")):
				brand = brand[2:].strip()
			print(brand)
			productName = webDriver.find_element_by_css_selector("span#productTitle").get_attribute('innerHTML').strip()
		except:
			try:
				data = webDriver.find_element_by_css_selector('a#bylineInfo')
				brand = data.get_attribute('href')
				brand = brand[1:len(brand)]
				print(brand)	
				productName = webDriver.find_element_by_css_selector("span#productTitle").get_attribute('innerHTML').strip()
			except:	
				pass

	# if(dept == "Apps &amp; Games"):
		
	# else:		
		
	print(productName)

	# prodDetails = webDriver.find_elements_by_css_selector("#productDetails_detailBullets_sections1 > tbody > tr > th")
	# for x in prodDetails:
	# 	print(x.get_attribute('innerHTML').strip())
	# 	if (x.get_attribute('innerHTML').strip() == "ASIN"):
	# 		ASIN = x.find_element_by_xpath("following-sibling::td").get_attribute('innerHTML').strip()
	# 		print(ASIN)
	# 		break

def getProduct(href, webDriver):
	webDriver.get(href)

def outputDeptToFile(dept, products):
	print('asf')

def driver():
	webDriver = webdriver.Chrome()
	webDriver.get("https://www.amazon.com/best-sellers/zgbs")
	Depts = list()
	hrefs = list()
	getAllDepts(webDriver, Depts, hrefs)
	# for dept in Depts:
	# 	print(dept)
	time.sleep(10)	
	for href in range(len(hrefs)):
		getDeptProducts(hrefs[href], Depts[href], webDriver)
	webDriver.close()

if __name__ == '__main__':
	#driver()
    connect_db()



'''
GET ALL DEPTS
'CLICK' ON EACH
GET ALL SUB DEPT - optional for now
SCRAPE ALL PRODUCT NAMES 
OUTPUT THEM TO A FILE 
''' 
