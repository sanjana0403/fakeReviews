import time
import json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


# TODO implement
browser = webdriver.Chrome("/usr/local/bin/chromedriver") #################### change here

file = open("rest_list.txt","r")
fout = open("user_url.txt",'w')

io = 1
for io in range(100) :
	x = file.readline()
	browser.get(x+'/reviews')
	print io,"rest ",x
	time.sleep(2)	
	
	allRevbutton = browser.find_element_by_xpath('//*[@id="selectors"]/a[2]')
	browser.execute_script("arguments[0].scrollIntoView(true);", allRevbutton);
	browser.execute_script("window.scrollBy(0,-70)");
	print allRevbutton.text
	allRevbutton.click()
		
	print "hello"
	time.sleep(5)
	print "slept"
	
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

	print "finding"
	
	results = browser.find_elements_by_css_selector('div.header.nowrap.ui.left > a')
	
	print "found"

	for p in results:
		user_url = p.get_attribute('href')
		print user_url
		fout.write(user_url)
		fout.write("\n")


browser.quit()
    
