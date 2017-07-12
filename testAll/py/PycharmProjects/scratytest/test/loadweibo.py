from selenium import webdriver
import time

webdriver = webdriver.PhantomJS(executable_path=r'C:\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')
webdriver.get('https://login.sina.com.cn/')

print(webdriver.current_url)
print(webdriver.title)

uname = webdriver.find_element_by_xpath('//form/div/ul/li[1]/input')
pw = webdriver.find_element_by_xpath('//form/div/ul/li[2]/input')
lbtn = webdriver.find_element_by_xpath('//form/div/ul/li[7]/a[1]/input')


uname.clear()
uname.send_keys("1262408238@qq.com")
pw.clear()
pw.send_keys("yang19880914")
lbtn.click()

time.sleep(3)

print(webdriver.current_url)
print(webdriver.title)

webdriver.quit()
