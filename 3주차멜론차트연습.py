import requests
from bs4 import BeautifulSoup

# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.melon.com/chart/index.htm',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
musics = soup.select('#lst50')

# movies (tr들) 의 반복문을 돌리기
for music in musics:
    # movie 안에 a 가 있으면,
    title_tag = music.select_one('td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a')
    rank_tag = music.select_one('td:nth-child(2) > div > span.rank')
    singer_tag = music.select_one('td:nth-child(6) > div > div > div.ellipsis.rank02 > a')
    if title_tag is not None:
        # a의 text를 찍어본다.
        print (rank_tag.text ,title_tag.text, singer_tag.text)