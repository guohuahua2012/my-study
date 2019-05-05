# coding = utf-8
from appium import webdriver
import time

desired_caps = {
                'platformName': 'Android',
                'platformVersion': '4.4.2',
                'deviceName': '25c8990c',
                'appPackage': '',
                'appActivity': '',
                #'unicodeKeyboard': True,
                #'resetKeyboard': True,
                'noReset': True #如果程序已经安装了，不需要重置，设置为True
               }

def swipeDown(driver, t=500, n=1):
    '''乡下滑动屏幕'''
    l = driver.get_window_size()
    x1 = l['width'] * 0.5           #x坐标
    y1 = l['height'] * 0.25         #起始y坐标
    y2 = l['height'] * 0.75         #终点y坐标
    for i in range(n):
        driver.swipe(x1, y1, x1, y2, t)

# 启动微信，等待加载
driver = webdriver.Remots('http://localhost:4723/wd/hub', desired_caps)
time.sleep(5)

#向下滑动，显示小程序图标
swipeDown(driver)
time.sleep(2)

# 点击打开小程序，
driver.find_element_by_id("com.tencent.mm:id/t7")[0].click()
time.sleep(3)


