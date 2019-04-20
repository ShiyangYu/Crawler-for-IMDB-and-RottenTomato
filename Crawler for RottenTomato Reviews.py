from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.request

S1E1 = 'https://www.rottentomatoes.com/tv/game-of-thrones/s01/e01/reviews/'


episodes = []
seasons = []
for i in range(1,11):
    if i < 10:
        a = "0" + str(i)      
    else:
        a = str(i)
    seasons.append('s'+a)
    episodes.append('e'+a)
seasons = seasons[:-3] ## GOT only has 7 seasons so far
urls  = []
for season in seasons:
    for episode in episodes:
        url = 'https://www.rottentomatoes.com/tv/game-of-thrones/'+season+ '/' +episode+'/reviews/'
        urls.append(url)
assert len(urls) == 70

urls = urls [:-3] ## season 7 only have 7 episodes

## every episodes may have sevaral review pages
pages = []
for url in urls:
    page2 = url + '?page=2'
    page3 = url + '?page=3'
    pages.append(url)
    pages.append(page2)
    pages.append(page3)
print(len(pages))

review = []  # create an empty list to store reviews 
epi_sea = []
epi = []
for url in pages:
    try:
        ourUrl=urllib.request.urlopen(url)
        soup=BeautifulSoup(ourUrl,'html.parser') 
        print('Python is crawling' + url[50:53] + url[54:57])
        for i in soup.find_all('td',{'style':'position:relative'}):  
            per_review=i.find('p')  # extract review
            review.append(per_review)  # append review
            epi_sea.append(url[50:53])
            epi.append(url[54:57])
    except:
        pass