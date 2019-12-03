import selenium
from selenium import webdriver
import time
import re
import csv
import string
import os

count = 0
"""def isEnglish(s):
    try:
        s.encode('ascii')
    except UnicodeEncodeError:
        return False
    else:
        return True"""

PROJECT_ROOT = os.path.abspath(os.path.dirname('chromedriver'))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")

driver = webdriver.Chrome(executable_path = DRIVER_BIN)
yt_link = input("Link to Youtube video: ")
print("-------------------------------------------------------------------------------------------------------------------")
driver.get(yt_link)
time.sleep(5)
title = driver.find_element_by_xpath('//*[@id="container"]/h1/yt-formatted-string').text
print("Video Title: " + title)
print("-------------------------------------------------------------------------------------------------------------------")

comment_section = driver.find_element_by_xpath('//*[@id="comments"]')
driver.execute_script("arguments[0].scrollIntoView();", comment_section)
time.sleep(7)

last_height = driver.execute_script("return document.documentElement.scrollHeight")
while True:
    
    # Scroll down to bottom
    #if (count <=10):
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    # Wait to load page
    time.sleep(2)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.documentElement.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height



driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")

emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  
                           u"\U0001F300-\U0001F5FF"
                           u"\U0001F680-\U0001F6FF"
                           u"\U0001F1E0-\U0001F1FF"
                           "]+", flags=re.UNICODE)

name_elems=driver.find_elements_by_xpath('//*[@id="author-text"]')
comment_elems = driver.find_elements_by_xpath('//*[@id="content-text"]')
num_of_names = len(name_elems)
print(num_of_names)
#for i in range(num_of_names):
target = open("Fifa5.txt", 'wb')
for i in range(num_of_names):
    username = name_elems[i].text    # .replace(",", "|")
    # username = emoji_pattern.sub(r'', username)
    # username = str(username).replace("\n", "---")
    comment = comment_elems[i].text    # .replace(",", "|")
    # comment = emoji_pattern.sub(r'', comment)
    # comment = str(comment).replace("\n", "---")
    
    #if isEnglish(comment) == False:
     #   comment = "NOT ENGLISH"
    target.write((username+ ': ' +comment + "\n"+"\n").encode())
    #print(username + ": " + comment) # comment.translate({ord(i):None for i in '' if i not in string.printable})
    #print("-------------------------------------------------------------------------------------------------------------------")
target.close

driver.close()