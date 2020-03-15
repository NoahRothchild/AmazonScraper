from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
from selenium.webdriver.common.by import By

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
	
	if(dept == "Apps &amp; Games"):
		data = webDriver.find_element_by_id('brand')
		brand = data.get_attribute('innerHTML').strip()
		print(brand)
	else:
		try:
			data = webDriver.find_element_by_css_selector('a#bylineInfo')
			brand = data.get_attribute('innerHTML').strip()
			if(brand[0:4] == "by\n\n"):
				brand = brand[4:len(brand)]
			print(brand)
		except:
			try:
				data = webDriver.find_element_by_css_selector('a#bylineInfo')
				brand = data.get_attribute('href')
				brand = brand[1:len(brand)]
				print(brand)	
			except:	
				pass
# <a id="brand" class="a-link-normal" href="/Marino-Avenue/b/ref=w_bl_sl_l_s_ap_web_12247642011?ie=UTF8&amp;node=12247642011&amp;field-lbr_brands_browse-bin=Marino+Avenue"><img alt="" src="https://images-na.ssl-images-amazon.com/images/I/01WGRzbbtcL._SR120,50_.jpg" id="brand"></a>


		#Get Books
		# booksCheck1 = webDriver.find_element_by_id("wayfinding-breadcrumbs_feature_div")
		# booksCheck2 = booksCheck1.find_element_by_class_name("a-list-item")
		# booksCheck3 = booksCheck2.find_element_by_tag_name("a")
		# if(booksCheck3.get_attribute('innerHTML').strip()=="Books"):
		# 	getPub1 = webDriver.find_element_by_id("bylineInfo")
		# 	getPub2 = getPub1.find_element_by_css_selector("#bylineInfo > span:nth-child(2)")
		# 	getPub3 = getPub2.find_element_by_tag_name("a")
		# 	brand = getPub3.get_attribute('innerHTML').strip()
		# 	print(brand)
		# else:
		# 	try:		
		# 		data = webDriver.find_element_by_id('bylineInfo')
		# 		print(data.get_attribute('innerHTML'))
		# 		brand = data.getText()
		# 		print(brand.stript())
		# 	except:
		# 		try:
		# 			data = webDriver.find_element_by_id('brand')
		# 			print(data.get_attribute('innerHTML').stript())	
		# 		except:
		# 			brand = "Could not get brand"
		# 			print(brand)
		# 			print(href)
		# 			# time.sleep(100)

	# outputDeptToFile(dept_name, products)
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
	for href in range(0,len(hrefs)):
		getDeptProducts(hrefs[href], Depts[href], webDriver)
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
