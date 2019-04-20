from selenium import webdriver
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

source = ['https://www.imdb.com/title/tt1480055/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt1668746/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt1829962/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt1829963/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt1829964/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt1837862/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt1837863/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt1837864/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt1851398/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt1851397/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt1971833/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt2069318/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt2070135/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt2069319/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt2074658/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt2085238/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt2085239/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt2085240/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt2084342/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt2112510/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt2178782/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt2178772/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt2178802/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt2178798/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt2178788/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt2178812/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt2178814/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt2178806/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt2178784/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt2178796/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt2816136/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt2832378/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt2972426/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt2972428/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt3060856/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt3060910/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt3060876/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt3060782/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt3060858/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt3060860/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt3658012/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt3846626/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt3866836/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt3866838/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt3866840/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt3866842/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt3866846/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt3866850/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt3866826/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt3866862/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt3658014/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt4077554/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt4131606/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt4283016/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt4283028/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt4283054/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt4283060/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt4283074/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt4283088/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt4283094/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt5654088/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt5655178/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt5775840/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt5775846/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt5775854/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt5775864/reviews?ref_=tt_ql_3',
 'https://www.imdb.com/title/tt5775874/reviews?ref_=tt_ql_3']

epi = []
title = [] 
review = []
rate =  []
date = []
username = []
## use 'selenium' to click 'next page' in website
browser = webdriver.Chrome(r'C:\Users\Yushi\Desktop\python\chromedriver')
while  True:
    for url in source:
        browser.implicitly_wait(30)
        browser.get(url)
        soup_level1=BeautifulSoup(browser.page_source, 'lxml')
        for item in soup_level1.find_all(class_="review-container"):
            if len(review) % 20 == 0:
                try:
                    python_button = browser.find_element_by_id('load-more-trigger') 
                    python_button.click() 
                except:
                    pass
                print('Already crawl %d reviews' % len(title))   
            soup_level2=BeautifulSoup(browser.page_source, 'lxml')
            review_title = item.find(class_="title").text
            review_content = item.find(class_="text").text
            review_date = item.find('span',class_ = 'review-date').get_text()
            review_username = item.find('span',class_ = "display-name-link").get_text()
            episode = source.index(url) + 1
            epi.append(episode)
            title.append(review_title)
            review.append(review_content)
            date.append(review_date)
            username.append(review_username)
            try:
                rating = item.find(class_="point-scale").previous_sibling.text
            except:
                rating = ""
            rate.append(rating)  
            