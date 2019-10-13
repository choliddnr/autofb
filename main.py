from selenium import webdriver
import time

class facebook:
	def __init__(self, email, password, dir):
		self.email = email
		self.password = password
		self.dir = dir
		chrome_options = webdriver.ChromeOptions()
		prefs = {"profile.default_content_setting_values.notifications" : 2}
		chrome_options.add_experimental_option("prefs",prefs)
		chrome_options.add_argument("user-data-dir="+self.dir)
		self.driver = webdriver.Chrome(chrome_options=chrome_options)

	def login(self):
		driver = self.driver
		driver.get('http://facebook.com')
		driver.find_elements_by_xpath("//input[@name='email']")[0].send_keys(self.email)
		driver.find_elements_by_xpath("//input[@name='pass']")[0].send_keys(self.password)
		driver.find_elements_by_xpath("//button[@name='login']")[0].click()
		

fb = facebook('ecosy.corp@gmail.com', 'EcosyCorp001', 'ecosy')
fb.login()

time.sleep(10)

# driver.quit()
