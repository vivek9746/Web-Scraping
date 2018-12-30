from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import choice
import requests
from bs4 import BeautifulSoup


driver = webdriver.Chrome(executable_path="")
url="https://gdpd.tk/index.php"
name=""
pwd=""
driver.get(url)
loginBtn = driver.find_element_by_id("loginBtn")
loginBtn.click()
nameinput=driver.find_element_by_name("userid")
password=driver.find_element_by_xpath('//*[@id="login-form"]/input[2]')
nameinput.send_keys(name)
password.send_keys(pwd)
aclogin=driver.find_element_by_name("btn-login")
aclogin.click()
newUrl=driver.current_url
checkrespBtn=driver.find_element_by_xpath('//*[@id="bodyProfile"]/a[1]/input')
checkrespBtn.click()

newUrl=driver.current_url

clas=driver.find_element_by_id('answers')
clasdown=clas.find_elements_by_class_name('ansx')
print(clasdown)
for classes in clasdown:
    print(classes.text)
    print("\n")

driver.close()
