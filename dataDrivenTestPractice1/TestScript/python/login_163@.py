#encoding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import traceback

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://mail.163.com/")
try:
    wait = WebDriverWait(driver,10,0.5) # 显示等待
    iframe = driver.find_element_by_xpath("//iframe[@frameborder='0']") # 切换到用户名和密码输入框所在的frame元素
    driver.switch_to.frame(iframe)
    name = wait.until(lambda x:x.find_element_by_xpath("//input[@data-placeholder='邮箱帐号或手机号码' and @name='email']"))
    name.send_keys("guohuahua_2012")
    password = wait.until(lambda x:x.find_element_by_xpath("//input[@data-placeholder='输入密码']"))
    password.send_keys("Gwx123456")
    submit = wait.until(lambda x:x.find_element_by_xpath("//a[@id='dologin']"))
    submit.click()
    driver.switch_to.default_content()
    time.sleep(10)

    page = driver.page_source
    print(page)
    assert u"网易邮箱6.0版" in driver.page_source, "no exist in page_source"
    address_book_link = wait.until(lambda x:x.find_element_by_xpath("//div[@id='_mail_tabitem_1_4text']"))
    address_book_link.click()

    #assert u"新建联系人" in driver.page_source
    # 点击【新建联系人】按钮
    add_contact_button = wait.until(lambda x:x.find_element_by_xpath("//div[@class='nui-toolbar-item']"))
    add_contact_button.click()
    # 输入姓名
    contact_name = wait.until(lambda x:x.find_element_by_xpath("//input[@id='input_N']"))
    contact_name.send_keys(u"郭春华")
    time.sleep(3)
    # 输入邮箱号
    #contact_email = wait.until(lambda x:x.find_element_by_xpath("/html/body/div[4]/div[2]/div/div/div[1]/div/div[1]/div[1]/dl/dd/div/input"))
    #contact_email.send_keys("371118530@qq.com")
    # 勾选为星标联系人
    contact_is_star = wait.until(lambda x:x.find_element_by_xpath("//input[@id='fly2']"))
    contact_is_star.click()
    # 输入手机号
    contact_phone = wait.until(lambda x:x.find_element_by_xpath("//input[@class='nui-ipt-input']"))
    contact_phone.send_keys("18926475276")
    # 输入备注信息
    contact_other_info = wait.until(lambda x:x.find_element_by_xpath("//textarea[@id='nui-ipt-input']"))
    contact_other_info.send_keys(u"本人")
    # 点击【确定】按钮
    contact_save_button = wait.until(lambda x:x.find_element_by_xpath("//span[@class='nui-btn-text']"))
    contact_save_button.click()
except TimeoutException as e:
    # 捕获TimeoutException异常
    print(traceback.format_exc())
except NoSuchElementException as e:
    # 捕获NoSuchElementException异常
    print(traceback.print_exc())
except Exception as e:
    # 捕获其他异常
    print(traceback.print_exc())







