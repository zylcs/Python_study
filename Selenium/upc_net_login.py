from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium .webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
def upc_net_login(num,pwd):
	chrome_options = Options()
	chrome_options.add_argument('--headless')
	driver = webdriver.Chrome(executable_path='E:\Office worke\chormedrive\chromedriver.exe',options=chrome_options)
	driver.get('http://wlan.upc.edu.cn')
	driver.find_element_by_id('username').clear()
	driver.find_element_by_id('username').send_keys(num)
	# js = "document.getElementById('pwd_tip').removeAttribute('readonly')"
	# driver.execute_script(js)
	js = "document.getElementById(\"pwd\").style.display='block';" #由于密码框被设置为不可见，selenium无法定位，故应该先设置其可见
	driver.execute_script(js)  #执行js
	wait = WebDriverWait(driver, 10)
	wait.until(EC.visibility_of_element_located((By.ID,"pwd")))  #等待密码框加载出来 可以不加
	driver.find_element_by_id('pwd').clear()
	password= driver.find_element_by_id("pwd")
	#ActionChains(driver).move_to_element(password)
	# driver.execute_script('document.getElementById("pwd").value=pwd)
	driver.find_element_by_id('pwd').send_keys(pwd)
	driver.find_element_by_id('xiala').click()
	time.sleep(0.5)
	driver.find_element_by_id('_service_4').click()
	driver.find_element_by_id('loginLink').click()
	driver.close()
if __name__ == '__main__':
  num=input('请输入账号: ')
  pwd=input('请输入密码: ')
	upc_net_login(num,pwd)
