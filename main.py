from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime as dt
import time
import csv


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
		driver.find_elements_by_xpath("//input[@value='Login']")[0].click()

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
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(3)
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		print('get like')
		likes = driver.find_elements_by_xpath("//a[contains(@data-testid, 'UFI2ReactionLink')]")
		print(len(likes))

		for like in likes:
			print(like)
			ActionChains(driver).move_to_element(like).perform()
			like.click()
			print('klikked')
			time.sleep(10)

	def collect_post(self, groups_id, last_crawl):
		driver = self.driver
		# print(group_id)
		data = []
		data.append(["Timestamp", "By", "Title", "Price", "Desc"])
		for group_id in groups_id:
			driver.get('https://www.facebook.com/groups/'+group_id)
			posts =  driver.find_elements_by_xpath("//div[@class='_5pcr userContentWrapper']")
			i = 0
			while len(posts) < 250:
				i += 1
				driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
				time.sleep(2)
				posts =  driver.find_elements_by_xpath("//div[@class='_5pcr userContentWrapper']")
				print(len(posts))
				if i > 25:
					break

			
			print(len(posts))
			
			i = 1
			for post in posts:
				ActionChains(driver).move_to_element(post).perform()
				try:
					by = post.find_element_by_css_selector("span a").get_attribute("title")
					timestamp = post.find_element_by_class_name("timestamp").get_attribute("title")
				except Exception as e:
					continue

				try:
					price = post.find_element_by_css_selector("div.qzhwtbm6.knvmm38d span span span").text
				except Exception as e:
					price = ""	

				try:
					title = post.find_element_by_css_selector("div.qzhwtbm6.knvmm38d span div span span").text
				except Exception as e:
					title = ""

				try:
					desc = post.find_element_by_css_selector("div.userContent div p").text
					print('div p')
				except Exception as e:
					desc = ""

				if desc == "":
					try:	
						desc = post.find_element_by_css_selector("div.userContent div span:nth-child(2) span").text
						print('span')
					except Exception as e:
						continue
					
				try:
					# print(timestamp, type(timestamp))
					post_time = dt.strptime(timestamp, '%d/%m/%y %H.%M')
					if post_time > last_crawl:
						print(post_time, last_crawl, post_time < last_crawl)
						print(i, by, title, price, timestamp)
						print(desc.replace("\n", " "))
						# 	print('old')
						# print(post_time)
						print('\n')
						data.append([timestamp, by, title, price, desc.replace("\n", " ")])
						i += 1
					else:
						continue

				except Exception as e:
					print(e)
				# print(data)
		print(data)
		current_time = str(dt.now().strftime("%m_%d_%y_%I_%M_%p"))
		# current_time = ""
		with open('data_'+current_time+'.csv', 'w', newline='') as file:
			writer = csv.writer(file, delimiter=';')
			writer.writerows(data)

		# print(data)

laptop_groups = []
laptop_groups.append('177555225978002')
laptop_groups.append('1377006995866632')
laptop_groups.append('1388185871503108')
laptop_groups.append('1600132223650431')
laptop_groups.append('372532546289268')
laptop_groups.append('ipanlaptop')
laptop_groups.append('565807200279413')
laptop_groups.append('malangkomputer')
laptop_groups.append('1012779115493280')
laptop_groups.append('jual.beli.laptop.malang')
# laptop_groups.append('bocahjagongcommunity')
# laptop_groups.append('486077118262347')
# laptop_groups.append('1867840613500291')
# laptop_groups.append('323355611094325')
# laptop_groups.append('1624924917769545')
# laptop_groups.append('136209003756450')
# laptop_groups.append('307970376064687')
# laptop_groups.append('746773775440421')
# laptop_groups.append('1011152592245929')
# laptop_groups.append('1240656179396195')
# laptop_groups.append('1552417831689244')
# laptop_groups.append('610230812352888')
# laptop_groups.append('197691324454729')
# laptop_groups.append('471254656301182')





fb = facebook('ecosy.corp@gmail.com', 'EcosyCorp002', 'ecosy')
# fb.login()
# fb.add_group_member('1878596892377482')
last_crawl = dt.strptime('02/29/20, 12:00 AM', '%m/%d/%y, %I:%M %p')
fb.collect_post(laptop_groups, last_crawl)
# fb.like_beranda_posts()
# time.sleep(5)


# print(laptop_groups)


# d1_str = '02/03/20 16.24'
# d2_str = '12/29/19, 3:41 AM'
# d1 = dt.strptime(d1_str, '%d/%m/%y %H.%M')
# # d2 = dt.strptime(d2_str, '%m/%d/%y, %I:%M %p')
# print(d1, type(d1)) 
# current_time = dt.now().strftime("%m/%d/%y, %I:%M %p")
# print(str(current_time))
# # Comparing the dates will return 
# # either True or False 
# print(dt.now())
# print("d1 is greater than d2 : ", d1 > d2) 
# print("d1 is less than d2 : ", d1 < d2) 
# print("d1 is not equal to d2 : ", d1 != d2)
# print(d2 - d1)