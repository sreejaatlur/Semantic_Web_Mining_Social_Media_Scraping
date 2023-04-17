
import urllib.request
from bs4 import BeautifulSoup as bs
import pandas as pd
import json
import time
import re
import datetime
from selenium.webdriver.common.by import By


def openComment(browser):    
    moreComment = browser.find_elements(By.CLASS, "//span[contains(@class,'d2edcug0 hpfvmrgz qv66sw1b c1et5uql oi732d6d ik7dh3pa ht8s03o8 a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d9wwppkn fe6kdd0r mau55g9w c8b282yb iv3no6db jq4qci2q a3bd9o3v lrazzd5p m9osqain') and starts-with(text(), 'View') and contains(text(), 'more comment')]")
    if len(moreComment) > 0:
        count = 0
        for i in moreComment:
            action=ActionChains(browser)
            try:
                action.move_to_element(i).click().perform()
                count += 1
            except:
                try:
                    browser.execute_script("arguments[0].click();", i)
                    count += 1
                except:
                    continue
        if len(moreComment) - count > 0:
            print('moreComment issue:', len(moreComment) - count)
        time.sleep(1)
    else:
        pass

      
def openReply(browser):
    replies = browser.find_elements(By.XPATH, "//div[@class='rq0escxv l9j0dhe7 du4w35lb j83agx80 cbu4d94t pfnyh3mw d2edcug0 hpfvmrgz n8tt0mok hyh9befq r8blr3vg jwdofwj8 g0qnabr5']")
    if len(replies) > 0:
        count = 0
        for i in replies:
            action=ActionChains(browser)
            try:
                action.move_to_element(i).click().perform()
                count += 1
            except:
                try:
                    browser.execute_script("arguments[0].click();", i)
                    count += 1
                except:
                    continue
        if len(replies) - count > 0:
            print('replies issue:', len(replies) - count)
        time.sleep(1)
    else:
        pass


def openReply2(browser):
    replies = browser.find_elements(By.XPATH, "//span[@class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql oi732d6d ik7dh3pa ht8s03o8 a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d9wwppkn fe6kdd0r mau55g9w c8b282yb iv3no6db jq4qci2q a3bd9o3v lrazzd5p m9osqain' and contains(text(),'more repl')]")
    if len(replies) > 0: 
        count = 0
        for i in replies:
            action=ActionChains(browser)
            try:
                action.move_to_element(i).click().perform()
                count += 1
            except:
                try:
                    browser.execute_script("arguments[0].click();", i)
                    count += 1
                except:
                    continue
        if len(replies) - count > 0:
            print('replies2 issue:', len(replies) - count)
        time.sleep(1)
    else:
        pass

      
def openSeeMore(browser):
    readMore = browser.find_elements(By.XPATH, "//div[contains(@class,'oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl oo9gr5id gpro0wi8 lrazzd5p') and contains(text(), 'See More')]")
    if len(readMore) > 0:    
        count = 0
        for i in readMore:
            action=ActionChains(browser)
            try:
                action.move_to_element(i).click().perform()
                count += 1
            except:
                try:
                    browser.execute_script("arguments[0].click();", i)
                    count += 1
                except:
                    continue
        if len(readMore) - count > 0:
            print('readMore issue:', len(readMore) - count)
        time.sleep(1)
    else:
        pass

def getBack(browser):
    if not browser.current_url.endswith('reviews'):
        print('redirected!!!')
        browser.back()
        print('got back!!!')

def archiveAtEnd(browser, reviewList):
    browser.execute_script("window.scrollTo(0, -document.body.scrollHeight);") # scroll back to the top
    time.sleep(10)
        
    for idx, l in enumerate(reviewList):
        if idx % 10 == 0:
            if idx < 15:
                browser.execute_script("arguments[0].scrollIntoView();", reviewList[0])
            else:
                browser.execute_script("arguments[0].scrollIntoView();", reviewList[idx-15])
            
            time.sleep(1)
            try:
                browser.execute_script("arguments[0].scrollIntoView();", reviewList[idx+15])
            except:
                browser.execute_script("arguments[0].scrollIntoView();", reviewList[-1])

            time.sleep(1)
            browser.execute_script("arguments[0].scrollIntoView();", reviewList[idx])
            
            for r in range(2):
                time.sleep(3)
                try:
                    browser.execute_script("arguments[0].scrollIntoView();", reviewList[idx+5])
                    time.sleep(3)
                except:
                    browser.execute_script("arguments[0].scrollIntoView();", reviewList[-1])
                browser.execute_script("arguments[0].scrollIntoView();", reviewList[idx+r*3])
                time.sleep(3)
                with open(f'./PATH/{str(idx)}_{r}.html',"w", encoding="utf-8") as file:
                    source_data = browser.page_source
                    bs_data = bs(source_data, 'html.parser')
                    file.write(str(bs_data.prettify()))
                    print(f'written: {idx}_{r}')