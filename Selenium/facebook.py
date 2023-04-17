# selenium-related
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import requests

# other necessary ones
import urllib.request
from bs4 import BeautifulSoup as bs
import pandas as pd
import json
import time
import re
import datetime
from helper import *
import os
# set options as you wish
option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
option.add_argument("--disable-notifications")

with open('Selenium\\facebook_credentials.txt', encoding="utf8") as file:
    EMAIL = file.readline().split('=')[1].strip()
    PASSWORD = file.readline().split('=')[1].strip()
    
browser = webdriver.Chrome(executable_path="./chromedriver", options=option)
browser.get("http://facebook.com")
browser.maximize_window()
wait = WebDriverWait(browser, 60)

email_field = wait.until(EC.visibility_of_element_located((By.NAME, 'email')))
email_field.send_keys(EMAIL)
pass_field = wait.until(EC.visibility_of_element_located((By.NAME, 'pass')))
pass_field.send_keys(PASSWORD)
pass_field.send_keys(Keys.RETURN)

time.sleep(5)
browser.get('https://www.facebook.com/search/posts/?q=trump') # once logged in, free to open up any target page
time.sleep(5)

last_height = browser.execute_script("return document.body.scrollHeight")
postName = []
postContent = []
likes = []
comments = []
shares = []
start_time = time.time()

while time.time() - start_time < 40:
    # Scroll down to the bottom.
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load the page.
    time.sleep(3)
    # Calculate new scroll height and compare with last scroll height.
    posts = browser.find_elements(By.CSS_SELECTOR, "[role='article']")
    for post in posts:
        userIds = post.find_element(By.CSS_SELECTOR, "strong > span")
        postName.append(userIds.text)
        texts = post.find_element(By.CSS_SELECTOR, "[data-ad-preview='message']")
        postContent.append(texts.text)
        likess = post.find_element(By.CLASS_NAME, "x1n2onr6")
        number_of_likes = likess.find_element(By.CSS_SELECTOR, '.xt0b8zv.x1jx94hy.xrbpyxo.xl423tq > span')
        likes.append(number_of_likes.text)
        dynamics = likess.find_elements(By.CSS_SELECTOR, ".x193iq5w.xeuugli.x13faqbe.x1vvkbs.x1xmvt09.x1lliihq.x1s928wv.xhkezso.x1gmr53x.x1cpjm7i.x1fgarty.x1943h6x.xudqn12.x3x7a5m.x6prxxf.xvq8zen.xo1l8bm.xi81zsa")
        comments.append(0 if dynamics[1].text == '' else dynamics[1].text)
        shares.append(0 if dynamics[2].text == '' else dynamics[2].text)
print(len(postName))
print(len(postContent))
print(len(likes))
print(len(comments))
print(len(shares))
data = {'Post Name': postName,
         'Post Description': postContent,
         'Likes': likes,
         'Comments': comments,
         'Shares' : shares}
df = pd.DataFrame.from_dict(data)
df.to_csv('out.csv')











#     #target all the link elements on the page
# anchors = browser.find_elements(By.TAG_NAME, 'a')
# anchors = [a.get_attribute('href') for a in anchors]
# #narrow down all links to image links only
# anchors = [a for a in anchors if str(a).startswith("https://www.facebook.com/photo")]
# anchors = ['https://www.facebook.com/photo.php?fbid=604042241767524&set=pb.100064852595827.-2207520000.&type=3']

# for anchor in anchors:
#     page = requests.get(anchor)
#     soup = bs(page.content, "html.parser")
#     time.sleep(5)
#     all_posts=soup.find_all("div",{"class":"x1n2onr6"})
#     for post in all_posts:
#         f = post.find("span", {"class":"x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x4zkp8e x676frb x1nxh6w3 x1sibtaa x1s688f xzsf02u"})
#         print(f)
