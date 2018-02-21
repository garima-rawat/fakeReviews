from pymongo import MongoClient
import bson


import time
import json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
browser = webdriver.Chrome("/home/garima/Downloads/chromedriver")
#selectors > a.item.default-section-title.everyone.empty



Client = MongoClient()
db = Client['zomato']
collection = db['restaurants']



# def writeToJSONFile(path, fileName, data):
#     filePathNameWExt =  path  + fileName + '.json'
#     with open(filePathNameWExt, 'a') as f:
#         json.dump(data, f)

data = []

file = open("rest_list.txt","r")
fout = open("user_url.txt",'a')
io = 1
for io in range(50) :
	rest_url = file.readline()
	browser.get(rest_url+'/reviews')
	print io,"rest ",rest_url
	#ime.sleep(2)	
	#browser.get('https://www.zomato.com/ncr/jungle-jamboree-connaught-place-new-delhi/reviews')
	time.sleep(5)

	allRevbutton = browser.find_element_by_xpath('//*[@id="selectors"]/a[2]')
	browser.execute_script("arguments[0].scrollIntoView(true);", allRevbutton);
	browser.execute_script("window.scrollBy(0,-70)");
	print allRevbutton.text
	allRevbutton.click()
	time.sleep(5)
	while True:
	    try:
	    	loadMoreButton = browser.find_element_by_css_selector('div.load-more.bold.ttupper.tac.cursor-pointer.fontsize2')
	        time.sleep(2)
	        print loadMoreButton.text
	        browser.execute_script("arguments[0].scrollIntoView(true);", loadMoreButton);
	        browser.execute_script("window.scrollBy(0,-100)");
	        loadMoreButton.click()
	        time.sleep(5)
	    except Exception as e:
	        break

	name = []
	user_id = []
	user_url = []
	rating = []
	review_content = []
	review_time = []
	review_likes = []
	review_comments = []
	
	
	rest_name = browser.find_element_by_css_selector('div.ui.segment.res-header-overlay.vr > div > div.col-s-12.pr20 > div.row.mtop > div.col-l-12 > h1 > a').get_attribute('title')
	
	#rest_id = '18157384'
	#rest_url = 'https://www.zomato.com/ncr/jungle-jamboree-connaught-place-new-delhi' 
	j = 0

	i = 0
	for p in browser.find_elements_by_css_selector('div.header.nowrap.ui.left'):
		name.append(p.text)
		
	for p in browser.find_elements_by_css_selector('.left.bold.zdhl2.tooltip'):
		rating.append(p.get_attribute('aria-label')[6:])

	for p in browser.find_elements_by_css_selector(".rev-text"):
	 	review_content.append(p.text[6:])

	for p in browser.find_elements_by_css_selector('div.header.nowrap.ui.left > a'):
		user_id.append(p.get_attribute('data-entity_id'))

	for p in browser.find_elements_by_tag_name('time'):
		review_time.append(p.get_attribute('datetime'))

	for p in browser.find_elements_by_css_selector('div.ui.basic.label.stats-thanks.js-thank-count.js-activity-like-count'):
		review_likes.append(p.text)

	for p in browser.find_elements_by_css_selector('div.left.ui.tiny.labeled.button.comment-btn-to > div.ui.basic.label.stats-comment'):
		review_comments.append(p.text)
		
	for p in browser.find_elements_by_css_selector('div.header.nowrap.ui.left > a'):
		user_url.append(p.get_attribute('href'))
		i = i+1
		j=i


	obj = {}

	obj['rest_name'] = rest_name
	obj['rest_url'] = rest_url
	#obj['rest_id'] = rest_id = 0

	review_array = []

	print j

	for i in range(j):
		print i
		print name[i]
		print user_url[i]
		fout.write(user_url[i])
		fout.write("\n")
		# print rating[i]	
		# print user_id[i]
		# print user_url[i]
		#print review_content[i]

		review_obj = {}

		review_obj['name'] = name[i]
		review_obj['user_url'] = user_url[i]
		review_obj['user_id'] = user_id[i]

		review_obj['rating'] = rating[i]
		review_obj['review_content'] = review_content[i]
		review_obj['review_time'] = review_time[i]
		review_obj['review_likes'] = review_likes[i]
		review_obj['review_comments'] = review_comments[i]

		review_array.append(review_obj)

		#print obj
	obj['reviews'] = review_array

	collection.insert(obj);
	#data.append(obj)
		
#writeToJSONFile('/home/garima/Desktop/major/','user',data)
browser.quit()




#for i in browser.find_elements_by_css_selector('')

#reviews-container > div.notifications-content > div.res-reviews-container.res-reviews-area > div.zs-following-list > div:nth-child(10) > div > div.ui.segment.clearfix.brtop > div.ui.item.clearfix > div.item > div > div > div > div > div.header.nowrap.ui.left > a
#reviews-container > div.notifications-content > div.res-reviews-container.res-reviews-area > div.zs-following-list > div:nth-child(10) > div > div.ui.segment.clearfix.brtop > div.rev-text.mbot0	
#reviews-container > div.notifications-content > div.res-reviews-container.res-reviews-area > div.zs-following-list > div:nth-child(12) > div > div.ui.segment.clearfix.brtop > div.rev-text.mbot0 > div.ttupper.fs12px.left.bold.zdhl2.tooltip.icon-font-level-5
#reviews-container > div.notifications-content > div.res-reviews-container.res-reviews-area > div.zs-following-list > div:nth-child(12) > div > div.ui.segment.clearfix.brtop > div.ui.item.clearfix > div.item > div > div > div > div > div.header.nowrap.ui.left

# a = browser.find_element(By.XPATH,'//*[@id="reviews-container"]/div[1]/div[3]/div[1]/div[1]/div/div[1]').text

# name = browser.find_element(By.XPATH,'//*[@id="reviews-container"]/div[1]/div[3]/div[1]/div[1]/div/div[1]/div[3]/div[1]/div/div/div/div/div[1]/a').text
# print name

# user_id = browser.find_element(By.XPATH,'//*[@id="reviews-container"]/div[1]/div[3]/div[1]/div[1]/div/div[1]/div[3]/div[1]/div/div/div/div/div[1]/a').get_attribute('data-user_id')
# print user_id

# rating = browser.find_element(By.XPATH,'//*[@id="reviews-container"]/div[1]/div[3]/div[1]/div[1]/div/div[1]/div[4]/div[1]').get_attribute('aria-label')
# rating = rating[6:9]
# print rating

# user_url = browser.find_element(By.XPATH,'//*[@id="reviews-container"]/div[1]/div[3]/div[1]/div[1]/div/div[1]/div[3]/div[1]/div/div/div/div/div[1]/a').get_attribute('href')
# print user_url

# review_content = browser.find_element(By.XPATH,'//*[@id="reviews-container"]/div[1]/div[3]/div[1]/div[1]/div/div[1]/div[4]').text
# print review_content

# rest = 'Jungle Jamboree'
# rest_url = 'https://www.zomato.com/ncr/jungle-jamboree-connaught-place-new-delhi'

# obj = {}

# obj['name'] = name
# obj['user_url'] = user_url
# obj['user_id'] = user_id
# obj['rest'] = rest
# obj['rest_url'] = rest_url
# obj['rating'] = rating
# obj['review_content'] = review_content

# print "hello"
# print obj



# import time
# import json
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# browser = webdriver.Chrome("/home/garima/Downloads/chromedriver")
# #selectors > a.item.default-section-title.everyone.empty

# def writeToJSONFile(path, fileName, data):
#     filePathNameWExt =  path  + fileName + '.json'
#     with open(filePathNameWExt, 'a') as f:
#         json.dump(data,f)

# data = []

# file = open("rest_list.txt","r")
# io = 1
# for io in range(3) :
# 	x = file.readline()
# 	browser.get(x+'/reviews')
# 	print io,"rest ",x
# 	# time.sleep(2)	
# 	# browser.get('https://www.zomato.com/ncr/jungle-jamboree-connaught-place-new-delhi/reviews')
# 	# time.sleep(2)	
# 	# while  True:
# 	# 	try:
# 	# 		allRevbutton = browser.find_element_by_xpath('//*[@id="selectors"]/a[2]')
# 	# 		browser.execute_script("arguments[0].scrollIntoView(true);", allRevbutton);
# 	# 		browser.execute_script("window.scrollBy(0,-100)");
# 	# 		allRevbutton.click()
# 	# 	except Exception as e:
# 	# 		break
	
# 	# time.sleep(5)
# 	#######browser.get('https://www.zomato.com/ncr/jungle-jamboree-connaught-place-new-delhi/reviews')

# 	while True:
# 	    try:
# 	    	loadMoreButton = browser.find_element_by_css_selector('div.load-more.bold.ttupper.tac.cursor-pointer.fontsize2')
# 	        time.sleep(2)
# 	        print loadMoreButton.text
# 	        browser.execute_script("arguments[0].scrollIntoView(true);", loadMoreButton);
# 	        browser.execute_script("window.scrollBy(0,-100)");
# 	        loadMoreButton.click()
# 	        time.sleep(5)
# 	    except Exception as e:
# 	        break

# 	name = []
# 	user_id = []
# 	user_url = []
# 	rating = []
# 	review_content = []
# 	review_time = []
# 	review_likes = []
# 	review_comments = []
# 	rest_name = browser.find_element_by_css_selector('div.ui.segment.res-header-overlay.vr > div > div.col-s-12.pr20 > div.row.mtop > div.col-l-12 > h1 > a').get_attribute('title')
# 	rest_id = '18157384'
# 	#rest_url = 'https://www.zomato.com/ncr/jungle-jamboree-connaught-place-new-delhi' 
# 	j = 0

# 	i = 0
# 	for p in browser.find_elements_by_css_selector('div.header.nowrap.ui.left'):
# 		name.append(p.text)
		
# 	for p in browser.find_elements_by_css_selector('.left.bold.zdhl2.tooltip'):
# 		rating.append(p.get_attribute('aria-label')[6:])


# 	# div_block = browser.find_elements_by_css_selector('.ui.segment.brtop')
# 	# for p in div_block:
# 	# 	try:
# 	# 		revexpand = p.find_element_by_class_name('rev-text-expand')
# 	# 		# print revexpand.text
# 	# 		readMoreButton = revexpand.find_element_by_class_name('read-more')
# 	# 		# print readMoreButton.text
# 	# 		browser.execute_script("arguments[0].scrollIntoView(true);", readMoreButton);
# 	# 		browser.execute_script("window.scrollBy(0,-100)");
# 	# 		readMoreButton.click()
# 	# 		# print r.text
# 	# 		time.sleep(5)
# 	# 		rev = p.find_element_by_class_name('rev-text')
# 	# 		review_content.append(rev)

# 	# 		print "in try"
# 	# 	except:
# 	# 		rev = p.find_element_by_class_name('rev-text')
# 	# 		review_content.append(p.text[6:])
# 	# 		print "in except"

	
# 	for p in browser.find_elements_by_css_selector(".rev-text"):
# 	 	review_content.append(p.text[6:])

# 	for p in browser.find_elements_by_css_selector('div.header.nowrap.ui.left > a'):
# 		user_id.append(p.get_attribute('data-entity_id'))

# 	for p in browser.find_elements_by_tag_name('time'):
# 		review_time.append(p.get_attribute('datetime'))

# 	for p in browser.find_elements_by_css_selector('div.ui.basic.label.stats-thanks.js-thank-count.js-activity-like-count'):
# 		review_likes.append(p.text)

# 	for p in browser.find_elements_by_css_selector('div.left.ui.tiny.labeled.button.comment-btn-to > div.ui.basic.label.stats-comment'):
# 		review_comments.append(p.text)
		
# 	for p in browser.find_elements_by_css_selector('div.header.nowrap.ui.left > a'):
# 		user_url.append(p.get_attribute('href'))
# 		i = i+1
# 		j=i

					
# 	obj = {}

# 	obj['rest_name'] = rest_name
# 	obj['rest_url'] = x #rest_url
# 	#obj['rest_id'] = rest_idi = 0

# 	review_array = []

# 	print j

# 	for i in range(j):
# 		print i
# 		print name[i]
# 		# print rating[i]	
# 		# print user_id[i]
# 		# print user_url[i]
# 		print review_content[i]

# 		review_obj = {}

# 		review_obj['name'] = name[i]
# 		review_obj['user_url'] = user_url[i]
# 		review_obj['user_id'] = user_id[i]

# 		review_obj['rating'] = rating[i]
# 		review_obj['review_content'] = review_content[i]
# 		review_obj['review_time'] = review_time[i]
# 		review_obj['review_likes'] = review_likes[i]
# 		review_obj['review_comments'] = review_comments[i]

# 		review_array.append(review_obj)

# 		#print obj
# 	obj['reviews'] = review_array
# 	data.append(obj)
		
# writeToJSONFile('/home/garima/Desktop/major/','user',data)
# browser.quit()




# #for i in browser.find_elements_by_css_selector('')

# #reviews-container > div.notifications-content > div.res-reviews-container.res-reviews-area > div.zs-following-list > div:nth-child(10) > div > div.ui.segment.clearfix.brtop > div.ui.item.clearfix > div.item > div > div > div > div > div.header.nowrap.ui.left > a
# #reviews-container > div.notifications-content > div.res-reviews-container.res-reviews-area > div.zs-following-list > div:nth-child(10) > div > div.ui.segment.clearfix.brtop > div.rev-text.mbot0	
# #reviews-container > div.notifications-content > div.res-reviews-container.res-reviews-area > div.zs-following-list > div:nth-child(12) > div > div.ui.segment.clearfix.brtop > div.rev-text.mbot0 > div.ttupper.fs12px.left.bold.zdhl2.tooltip.icon-font-level-5
# #reviews-container > div.notifications-content > div.res-reviews-container.res-reviews-area > div.zs-following-list > div:nth-child(12) > div > div.ui.segment.clearfix.brtop > div.ui.item.clearfix > div.item > div > div > div > div > div.header.nowrap.ui.left

# # a = browser.find_element(By.XPATH,'//*[@id="reviews-container"]/div[1]/div[3]/div[1]/div[1]/div/div[1]').text

# # name = browser.find_element(By.XPATH,'//*[@id="reviews-container"]/div[1]/div[3]/div[1]/div[1]/div/div[1]/div[3]/div[1]/div/div/div/div/div[1]/a').text
# # print name

# # user_id = browser.find_element(By.XPATH,'//*[@id="reviews-container"]/div[1]/div[3]/div[1]/div[1]/div/div[1]/div[3]/div[1]/div/div/div/div/div[1]/a').get_attribute('data-user_id')
# # print user_id

# # rating = browser.find_element(By.XPATH,'//*[@id="reviews-container"]/div[1]/div[3]/div[1]/div[1]/div/div[1]/div[4]/div[1]').get_attribute('aria-label')
# # rating = rating[6:9]
# # print rating

# # user_url = browser.find_element(By.XPATH,'//*[@id="reviews-container"]/div[1]/div[3]/div[1]/div[1]/div/div[1]/div[3]/div[1]/div/div/div/div/div[1]/a').get_attribute('href')
# # print user_url

# # review_content = browser.find_element(By.XPATH,'//*[@id="reviews-container"]/div[1]/div[3]/div[1]/div[1]/div/div[1]/div[4]').text
# # print review_content

# # rest = 'Jungle Jamboree'
# # rest_url = 'https://www.zomato.com/ncr/jungle-jamboree-connaught-place-new-delhi'

# # obj = {}

# # obj['name'] = name
# # obj['user_url'] = user_url
# # obj['user_id'] = user_id
# # obj['rest'] = rest
# # obj['rest_url'] = rest_url
# # obj['rating'] = rating
# # obj['review_content'] = review_content

# # print "hello"
# # print obj