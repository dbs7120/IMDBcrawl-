import requests
from bs4 import BeautifulSoup
import time
#import requests

count_t = time.time()



whole_url = ""
MAX_PAGE = 1

for page_number in range(1, MAX_PAGE+1):
    URL = 'https://www.imdb.com/search/title?groups=top_1000&sort=user_rating&page=' + str(page_number)
    #response = requests.get(URL)

html = BeautifulSoup(whole_url, 'html.parser')
#soup = BeautifulSoup(html, 'html.parser')

for tag in soup.findAll(True,{"class":["lister-item-header","Director:"]}):
    str=(tag.text.split())
    str=(' '.join(str))
    print(str)
    #print('\n')

#main > div > div > div.lister-list > div:nth-child(1) > div.lister-item-content > p:nth-child(5)

print('Running Time(second) : %.02f' % (time.time() - count_t))








