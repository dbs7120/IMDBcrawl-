import sys
import requests
from bs4 import BeautifulSoup
import time

count_t = time.time()

# 출력 txt 파일 UTF8형식 저장
file = open('imdb1000.txt', 'wt', encoding='UTF8')

MAX_PAGE = 20
html = ""

# pagination된 사이트이므로 for 문을통해 MAX_PAGE(=20)까지 반복하여 정보를 얻음
for page_number in range(1, MAX_PAGE+1):
    URL = 'https://www.imdb.com/search/title?groups=top_1000&sort=user_rating&page=' + str(page_number)
    response = requests.get(URL)    # requests.get()을 통해서 웹에 있는 소스 가져옴
    html = html + response.text     # 소스 누적

# soup객체를 통해 파싱 진행
soup = BeautifulSoup(html, 'html.parser')
find_tag = soup.find_all("", {"class": ["lister-item-header", "genre"]})    # 두종류의 html class


# 클롤링된 리스트를 스트링화 밑 정렬하여 텍스트파일에 입력
for tag in find_tag:
    txt = tag.text.split()
    txt = (' '.join(txt))
    file.write(txt)
    file.write('\n')

file.close()

# time 모듈을 통해 실행시간 측정(초단위)
print('Running Time(second) : %.02f' % (time.time() - count_t))







