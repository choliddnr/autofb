from selenium import webdriver
import time
 
def chrome_opt():
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument("user-data-dir=ecosy")
	return chrome_options


# The place we will direct our WebDriver to
url = 'http://facebook.com/'
options = chrome_opt()
driver = webdriver.Chrome(chrome_options=options)

# Directing the driver to the defined url
driver.get(url)

time.sleep(10)

driver.quit()
