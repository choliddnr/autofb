from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
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
		self.action = ActionChains(self.driver)

	def login(self):
		driver = self.driver
		driver.get('http://facebook.com')
		driver.find_elements_by_xpath("//input[@name='email']")[0].send_keys(self.email)
		driver.find_elements_by_xpath("//input[@name='pass']")[0].send_keys(self.password)
		driver.find_elements_by_xpath("//button[@name='login']")[0].click()

	def add_group_member(self, group_id):
		driver = self.driver
		self.group = group_id
		driver.get('https://www.facebook.com/groups/'+self.group+'/local_members/')
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(2)
		e_members = driver.find_elements_by_xpath("//button[contains(@class, 'FriendRequestAdd addButton') and not(contains(@class,'selected')) and not(contains(@class , 'hidden_elem'))]")
		print(len(e_members))
		time.sleep(2)
		n = 0
		mem = []
		for e in e_members:
			link_member = e.find_element_by_xpath("../../../../../../../ a").get_attribute("href")
			print(e,link_member)
			mem.append(link_member.replace('www', 'm'))
			n +=  1

		print(mem)
		e = 0
		while e < len(mem):
			print(e, mem[e])
			driver.get(mem[e])
			time.sleep(5)
			driver.find_element_by_xpath("//div[contains(@data-sigil, 'add-friend')]").click()
			print("added friend and wait 10 sec")
			time.sleep(10)
			driver.back()
			time.sleep(3)
			e += 1

	def like_beranda_posts(self):
		driver = self.driver
		driver.get('https://facebook.com')
		# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		# time.sleep(3)
		# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		print('get like')
		likes = driver.find_elements_by_xpath("//a[contains(@data-testid, 'UFI2ReactionLink')]")
		print(len(likes))

		for like in likes:
			print(like)
			ActionChains(driver).move_to_element(like).perform()
			like.click()
			print('klikked')
			time.sleep(10)

# <a aria-pressed="false" class=" _6a-y _3l2t  _18vj" data-testid="UFI2ReactionLink" href="#" role="button" tabindex="-1"><i alt="" class="_6rk2 img sp_ddXiTdIB8vm sx_44a25c"></i>Suka</a>



fb = facebook('ecosy.corp@gmail.com', 'EcosyCorp001', 'ecosy')
# fb.login()
# fb.add_group_member('1878596892377482')
# fb.add_group_member('1643677825657529')
fb.like_beranda_posts()
time.sleep(5)

