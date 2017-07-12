import os
import time
import urllib.request
import random
from PIL import Image
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

chromedriver = "C:\chromedriver_win32\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)
browser.get("http://www.gsxt.gov.cn/index.html")
input_text = browser.find_element_by_id('keyword')
search_btn = browser.find_element_by_id('btn_query')
input_text.clear()
input_text.send_keys("百度")
time.sleep(1)
search_btn.click()
time.sleep(3)

b_1 = [[0]*2]*52
b = [[0]*2]*52
url = ""
url_1 = ""

flagall = True
kkk = 0

while flagall:
    try:
        # if kkk > 0:
        #     fresh = browser.find_element_by_css_selector("div.gt_refresh_tips")
        #     ActionChains(browser).click(fresh).perform()
        #     print("click")
        time.sleep(6)
        print(flagall)
        #出现滑块
        cut_im = browser.find_elements_by_xpath("//div[@class='gt_cut_bg_slice']")
        cut_im_1 = browser.find_elements_by_xpath("//div[@class='gt_cut_fullbg_slice']")

        # after
        for t in range(0, len(cut_im)):
            cut_info = cut_im[t].get_attribute("style")
            infos = cut_info.split(";")

            for i in range(0, len(infos)):
                info = infos[i]
                if len(info) > 0:
                    a = info.split(":", 1)

                    if a[0].strip() == "background-image":
                        url = a[1][6:len(a[1]) - 2]
                        # print(url)
                    elif a[0].strip() == "background-position":
                        po = a[1].strip()
                        po0 = (0 - int(po.split(" ")[0].replace("px", "")))
                        po1 = (0 - int(po.split(" ")[1].replace("px", "")))
                        b[t] = [po0, po1]
                        # print(po0)
                        # print(po1)

        # ori
        for t in range(0, len(cut_im_1)):
            cut_info = cut_im_1[t].get_attribute("style")
            infos = cut_info.split(";")

            for i in range(0, len(infos)):
                info = infos[i]
                if len(info) > 0:
                    a = info.split(":", 1)

                    if a[0].strip() == "background-image":
                        url_1 = a[1][6:len(a[1]) - 2]
                        # print(url)
                    elif a[0].strip() == "background-position":
                        po = a[1].strip()
                        po0 = (0 - int(po.split(" ")[0].replace("px", "")))
                        po1 = (0 - int(po.split(" ")[1].replace("px", "")))
                        b_1[t] = [po0, po1]
                        # print(po0)
                        # print(po1)

        time.sleep(3)
        # 保存解析滑块图片
        utlo = "C:\\Users\\Administrator\\Desktop\\ori.webp"
        utla = "C:\\Users\\Administrator\\Desktop\\after.webp"
        urllib.request.urlretrieve(url_1, utlo)
        urllib.request.urlretrieve(url, utla)
        b_after = b
        b_ori = b_1

        imgo = Image.open(utlo)
        imgolast = imgo.copy()
        imgoori = imgo.copy()
        k = 26

        for i in range(0, len(b_ori)):
            t = b_ori[i]
            part1 = imgoori.crop((t[0], t[1], t[0]+10, t[1]+58))
            w = int(i % 26)
            h = int(i / 26)

            imgolast.paste(part1, (w*10, h*58, w*10+10, h*58+58))

        box = (0, 0, 260, 116)
        part1 = imgolast.crop(box)
        part1.save("C:\\Users\\Administrator\\Desktop\\oritest.webp", "WEBP")

        imga = Image.open(utla)
        imgalast = imga.copy()
        imgaori = imga.copy()

        for i in range(0, len(b_after)):
            t = b_after[i]
            part1 = imgaori.crop((t[0], t[1], t[0]+10, t[1]+58))
            w = int(i % 26)
            h = int(i / 26)

            imgalast.paste(part1, (w*10, h*58, w*10+10, h*58+58))

        box = (0, 0, 260, 116)
        part1 = imgalast.crop(box)
        part1.save("C:\\Users\\Administrator\\Desktop\\aftertest.webp", "WEBP")

        # 计算滑块距离
        ori = Image.open("C:\\Users\\Administrator\\Desktop\\oritest.webp")
        after = Image.open("C:\\Users\\Administrator\\Desktop\\aftertest.webp")

        (width, height) = ori.size
        flag = False

        distance = 0

        for i in range(0, width):
            for j in range(0, height):
                for x in range(0, 2):
                    if abs(ori.getpixel((i, j))[x] - after.getpixel((i, j))[x]) > 150:
                        distance = i - 7
                        print("distance:"+str(distance))
                        flag = True
                        break
                if flag:
                    break
            if flag:
                break

        # 移动滑块
        slider = browser.find_element_by_css_selector("div.gt_slider_knob.gt_show")
        # chain = ActionChains(browser)
        index = 0
        l = 0
        # print("new")
        while l < distance:
            index += 1
            # if index == 1:
            #     r = random.uniform(int(distance / 2), int(distance * 0.75)+1)
            # elif index == 2:
            #     r = random.uniform(int(distance) * 0.25, int(distance / 2))
            # elif index == 3:
            #     r = random.uniform(int(distance) * 0.25, int(distance / 2))
            # else:
            #     r = random.uniform(int(distance / 6), int(distance / 8))
            # r = random.uniform(distance+10, distance+50)
            r = random.uniform(5, 10)
            l += r
            print("l:"+str(l))
            if l >= distance:
                print("l:" + str(l))
                # chain.click_and_hold(slider).move_by_offset(r, 0)
                ActionChains(browser).click_and_hold(slider).move_by_offset(r, 0).perform()
                backdis = l - distance
                # t1 = random.uniform(int(backdis / 2), int(backdis * 0.75))
                # time.sleep(random.uniform(0.5, 1))
                # ActionChains(browser).click_and_hold(slider).move_by_offset(-t1, 0).perform()
                # t2 = backdis - t1 - random.uniform(0, 1)
                # time.sleep(random.uniform(0.5, 1))
                ActionChains(browser).click_and_hold(slider).move_by_offset(-backdis, 0).perform()
                # print(r)
                # print(m)
                break
            # chain.click_and_hold(slider).move_by_offset(r, 0)
            ActionChains(browser).click_and_hold(slider).move_by_offset(r, 0).perform()
            # time.sleep(random.uniform(0.5, 1))

        # chain.perform()
        # time.sleep(random.uniform(0.5, 1))
        ActionChains(browser).release().perform()
        kkk += 1
        # chain.move_to_element(slider).release()
    except NoSuchElementException as e:
        flagall = False

time.sleep(2)
time.sleep(20)
browser.quit()

