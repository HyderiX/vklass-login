PATH = ""

import os
from selenium import webdriver
from time import sleep

if not os.path.exists("credentials.txt"):
    print("Make a credentials file first")
    quit()
with open('credentials.txt', 'r') as f:
    credentials = f.readlines()
for line in credentials:
    credentials[credentials.index(line)] = line.strip()

driver = webdriver.Firefox(executable_path=PATH)

driver.get('https://vklass.se')

login = driver.find_element_by_xpath('/html/body/div/div/section/div[2]/div/div[1]/a[3]')
login.click()

uname = driver.find_element_by_xpath('//*[@id="Username"]')
uname.click()
uname.send_keys(credentials[0])
password = driver.find_element_by_xpath('//*[@id="Password"]')
password.click()
password.send_keys(credentials[1])

submitbutton = driver.find_element_by_xpath('/html/body/div/div/section/div[2]/div/form/div[4]/button')
submitbutton.click()







#driver.close()