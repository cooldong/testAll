from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.PhantomJS(executable_path=r'C:\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')
browser.get('https://passport.taobao.com/ac/password_find.htm?spm=a2107.1.0.0.TrRbh1&from_site=0&login_id=1231&lang=zh_CN')
time.sleep(5)  # 等待5s，关闭浏览器。

text = browser.find_element_by_css_selector("span.nc-lang-cnt")
slide = browser.find_element_by_css_selector("span.btn_slide")

print(slide.location)

ActionChains(browser).drag_and_drop_by_offset(slide, 598, 287).perform()
print(slide.location)

print(browser.title)
print(text.location)
print(text.size)
browser.quit()
