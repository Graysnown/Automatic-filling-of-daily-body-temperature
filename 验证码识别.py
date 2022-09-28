# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 22:15:42 2022

@author: Gray
"""
from selenium.webdriver.chrome.service import Service
import ddddocr
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
#webDriver位置
path = Service(r'')
driver = webdriver.Edge(service=path)
# 打开链接
driver.get('')
time.sleep(3)
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
   
