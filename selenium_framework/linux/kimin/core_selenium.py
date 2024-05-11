# import sys
# sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')
# import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service

import pickle, json, os
class Driver:
	def __init__(kimin, config, delay=20):
		kimin.driver = kimin.Get_Driver(config)
		kimin.tunggu = WebDriverWait(kimin.driver, delay)
	
	def Save_Cookie(kimin, path):
		with open(path, 'wb') as dataku:
			pickle.dump(kimin.driver.get_cookies(), dataku)
	
	def Load_Cookie(kimin, data):
		hasil = {'status':False}
		try:
			for i in data:
				kimin.driver.add_cookie(i)
			kimin.driver.refresh()
			hasil['status'] = True
		except Exception as e:
			hasil['error'] = e
		return hasil
	
	def Get_Driver(kimin, config):
		options = kimin.Set_Driver(config)
		c = [i for i in config['browser_config'] if '--binary=' in i]
		# if len(c) > 0:
			# s = Service(c[0].split('--binary=')[-1])
			# return webdriver.Chrome(service=s, options=options)
		return webdriver.Chrome(options=options)
	
	def Maximeze_Window(kimin):
		kimin.driver.maximize_window()
	
	def Minimaze_Window(kimin):
		kimin.driver.set_window_size(900, 500)
	
	def Switch_Window(kimin, mode='last'):
		try:
			handles = kimin.driver.window_handles
			for i in handles:
				kimin.driver.switch_to.window(i)
				if handles.index(i) == mode:
					break
			return True
		except Exception as e:
			return False
			# else
			# if mode == 'last':
	
	def Scroll_Funtion(kimin, elemen):
		kimin.driver.execute_script("arguments[0].scrollIntoView(true);", elemen)
	
	def Visit(kimin, url):
		try:
			kimin.driver.get(url)
			return True
		except TimeoutException:
			return False
		except:
			return False
	
	def Set_Driver(kimin, config):
		option = webdriver.ChromeOptions()
		# prefs = {"profile.default_content_setting_values.notifications" : 2}
		# option.add_experimental_option("prefs",prefs)
		# option.add_experimental_option("excludeSwitches", ["enable-automation"])
		# option.add_experimental_option("excludeSwitches", ["enable-logging"])
		# option.add_experimental_option('useAutomationExtension', False)
		for i in config['browser_config']:
			option.add_argument(i)
		if "extensi_path" in config:
			if not config['extensi_path'] == "":
				for i in os.listdir(config['extensi_path']):
					if i.split(".")[-1] == 'crx':
						option.add_extension(os.path.abspath(f"{config['extensi_path']}/{i}"))
		return option
	
	def Fill_XPATH(kimin, elemen, data):
		try:
			elemen = kimin.tunggu.until(EC.presence_of_element_located((By.XPATH, elemen)))
			for i in data:
				elemen.send_keys(i)
			return True
		except TimeoutException:
			return False
		except Exception as e:
			# print(e)
			return False
	
	def Wait_OpenWindow(kimin):
		try:
			kimin.tunggu.until(EC.number_of_windows_to_be(2))
			return True
		except TimeoutException:
			return False
		except:
			return False
	
	def Click_CSS(kimin, elemen):
		try:
			elemen = kimin.tunggu.until(EC.presence_of_element_located((By.CSS_SELECTOR, elemen)))
			elemen.click()
			return True
		except TimeoutException:
			return False
		except:
			return False
	
	def Click_XPATH(kimin, elemen):
		try:
			if isinstance(elemen, str):
				elemen = kimin.tunggu.until(EC.presence_of_element_located((By.XPATH, elemen)))
				elemen.click()
			else:
				elemen.click()
			return True
		except TimeoutException:
			return False
		except:
			return False
	
	def Click_ID(kimin, elemen):
		try:
			elemen = kimin.tunggu.until(EC.presence_of_element_located((By.ID, elemen)))
			elemen.click()
			return True
		except TimeoutException:
			return False
		except:
			return False
	
	def Click_Perform(kimin, elemen):
		try:
			aksi = ActionChains(kimin.driver)
			elemen = kimin.tunggu.until(EC.presence_of_element_located((By.XPATH, elemen)))
			aksi.move_to_element(elemen).click().perform()
			return True
		except TimeoutException:
			return False
		except:
			return False
	
	def Extract_Text(kimin, elemen):
		try:
			if isinstance(elemen, str):
				elemen = kimin.tunggu.until(EC.presence_of_element_located((By.XPATH, elemen))).text
			else:
				elemen.text
			return elemen
		except TimeoutException:
			return None
		except:
			return None
	
	def Elemen_Wait(kimin, elemen):
		try:
			kimin.tunggu.until(EC.presence_of_element_located((By.XPATH, elemen)))
			return True
		except TimeoutException:
			return False
		except:
			return False
	
	def Get_Attribute(kimin, elemen, data):
		try:
			elemen = kimin.tunggu.until(EC.presence_of_element_located((By.XPATH, elemen)))
			hasil = elemen.get_attribute(data)
			return hasil
		except TimeoutException:
			return None
		except:
			None
	
	def Get_Elemen_CSS(kimin, elemen):
		try:
			elemen = kimin.tunggu.until(EC.presence_of_element_located((By.CSS_SELECTOR, elemen)))
			return elemen
		except TimeoutException:
			return None
		except:
			return None
	
	def Get_Elemen(kimin, elemen, mode='default', n_elemen=None):
		try:
			if mode =='default':
				elemen = kimin.tunggu.until(EC.presence_of_element_located((By.XPATH, elemen)))
			elif mode == 'find':
				elemen = elemen.find_element(By.XPATH, n_elemen)
			return elemen
		except TimeoutException:
			return None
		
		except:
			return None