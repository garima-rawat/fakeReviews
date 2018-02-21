import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

j = 1
k = 1

file = open("rest_list.txt",'a')
driver = webdriver.Chrome("/home/garima/Downloads/chromedriver")
for i in range(22):

	driver.get("https://www.zomato.com/ncr/dine-out-in-connaught-place?ref_page=subzone&page="+ str(k))
	print i
	k = k+1

	results = driver.find_elements_by_xpath('//div[@class="col-s-12"]')

	for result in results:
	    restro = result.find_element_by_css_selector("a[class*=result-title]")
	    #title = restro.get_attribute('title')
	    url = restro.get_attribute('href')
	    print j,url
	    file.write(url)
	    file.write("\n")
	    j = j+1

driver.quit()

#search-results-container > div.search-pagination-top.clearfix.mtop > div.row > div.col-l-12 > div > div > a.paginator_item.next.item