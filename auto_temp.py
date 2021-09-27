import numpy as np
import pandas as pd
from datetime import datetime
from selenium import webdriver

# 讀取員工資料
users = pd.read_csv("users.csv")
users['temp'] = np.random.randint(350, 374, len(users)) / 10
print(users, end='\n\n')

with webdriver.Edge('msedgedriver.exe') as driver:
	print(datetime.now().strftime('[%H:%M:%S] '), 'WebDriver Activated')
	
	for idx, user in users.iterrows():
		print('------------------------------------------')
		print(user['name'], '|', user['id'], '|', user['vaccine'], '|', user['temp'])
		
		try:
			driver.get("https://zh.surveymonkey.com/r/EmployeeHealthCheck")

			# 同意
			driver.find_element_by_id('683674386_4495696088_label').click()

			# 工號
			driver.find_element_by_id('683674383').send_keys(user['id'])

			# 測量方式
			driver.find_element_by_id('683674388_4495696090_label').click()

			# 體溫
			driver.find_element_by_id('683674384').send_keys(str(user['temp']))

			# 症狀
			driver.find_element_by_id('683674400_4495696174').click()

			# 出國隔離
			driver.find_element_by_id('683674393_4495696115_label').click()

			# 疫苗
			if user['vaccine']:
				driver.find_element_by_id('683711504_4495952678_label').click()
			else:
				driver.find_element_by_id('683711504_4495952679_label').click()

			# 同住者
			driver.find_element_by_id('683674394_4495717677_label').click()

			# 足跡
			driver.find_element_by_id('683674398_4495718982_label').click()

			# PCR
			driver.find_element_by_id('683674395_4495696119_label').click()

			# 快篩
			driver.find_element_by_id('683674397_4495696166_label').click()

			# 屬實
			driver.find_element_by_id('683674385_4495696080_label').click()

			# 發送
			driver.find_element_by_class_name('btn.small.next-button.survey-page-button.user-generated.notranslate').click()

			print(datetime.now().strftime('[%H:%M:%S] '), 'Succeed!!')
		
		except:
			print(datetime.now().strftime('[%H:%M:%S] '), 'Failed!!')
			raise
