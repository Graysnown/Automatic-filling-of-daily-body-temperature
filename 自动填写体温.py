# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 08:23:36 2022

@author: Gray
"""

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import ddddocr
from selenium.webdriver.common.keys import Keys

#webDriver地址
path = Service(r'')
driver = webdriver.Edge(service=path)

#参数配置
URL = r""
username = ''
password =  ''
phoneNumber = ""
master = ""
def DoStart():
    #自动填充账号密码验证码
    driver.get(URL)
    time.sleep(3)
    driver.find_element(By.XPATH,'//*[@id="userName"]').send_keys(username)
    driver.find_element(By.XPATH,'//*[@id="password"]').send_keys(password)
    login_btn =driver.find_element(By.XPATH,'/html/body/div[1]/span/div[3]/div[2]/div[2]/div/div[1]/div/div/form/div[5]/button')

    while  True:
        try:
            autoSend()
        except ValueError:
            print('识别错误，正在重试……')
            DoStart()
        except UnboundLocalError:
            print('识别错误，正在重试……')
            DoStart()        
        else:
            break
            
    #点击登录
    # time.sleep(1)
    login_btn.click()
    time.sleep(1)
    
    #登陆后跳转填报
    time.sleep(8)
    #自动填报手机号和导员姓名
    driver.find_element(By.XPATH,'//*[@id="V1_CTRL10"]').click()
    driver.find_element(By.XPATH,'//*[@id="V1_CTRL10"]').send_keys(phoneNumber)
    driver.find_element(By.XPATH,'//input[contains(@value, "在校")]').click()
    time.sleep(1)
    #填充导员并确认
    driver.find_element(By.XPATH,"//input[contains(@id, 'activeInput')]").click()
    driver.find_element(By.XPATH,"//input[contains(@id, 'activeInput')]").send_keys(master)
    time.sleep(1)
    driver.find_element(By.XPATH,"//input[contains(@id, 'activeInput')]").send_keys(Keys.ENTER)
    #自动选择早中晚三个下拉选择菜单，并且选择特定值
    driver.find_element(By.XPATH,'//*[@id="V1_CTRL29"]/option[16]').click()
    driver.find_element(By.XPATH,'//*[@id="V1_CTRL30"]/option[16]').click()
    driver.find_element(By.XPATH,'//*[@id="V1_CTRL89"]/option[16]').click()
    
    time.sleep(1)
    driver.find_element(By.XPATH,'//*[@id="V1_CTRL132"]').click()#同意
    time.sleep(1)
    driver.find_element(By.XPATH,'/html/body/div[4]/form/div/div[3]/div[3]/div[2]/ul/li/a').click()#提交
    
    time.sleep(5)
    driver.quit()
    
def autoSend():
    yzm_input = driver.find_element(By.XPATH,'//*[@id="captcha"]')
    #验证码识别
    driver.find_element(By.XPATH,'//*[@id="root"]/span/div[3]/div[2]/div[2]/div/div[1]/div/div/form/div[3]/div/div/span/div/div[2]/div/img').screenshot('a.png')
    ocr = ddddocr.DdddOcr()
    with open('a.png', 'rb') as f:
        img_bytes = f.read()
        f.close()
        res = ocr.classification(img_bytes)
        print(res)

    if'+'in res:
        a, b = res.split('+')
        a = int(a)
        b = int(b)
        zhi = a + b
        print(zhi)
    if'-'in res:
        a, b = res.split('-')
        a = int(a)
        b = int(b)
        zhi = a - b
        print(zhi)
    if'*'in res:
        a, b = res.split('*')
        a = int(a)
        b = int(b)
        zhi = a * b
        print(zhi)
    if'/'in res:
        a, b = res.split('/')
        a = int(a)
        b = int(b)
        zhi = a / b
        print(zhi)
    yzm_input.send_keys(zhi) 
    
    
    #主入口
if __name__ == "__main__":
    print("程序运行中……")
    DoStart()
    print("填报完成，请自行查看结果")
    print("若成功填报，则无法重复进入填报页面")