import requests
from bs4 import BeautifulSoup

# 1단계: 페이지 가져오기
response = requests.get('https://search.daum.net/search?w=news&q=%EC%A3%A0%EC%8A%A4%EB%B0%94')
response.content

# 2단계: 데이터 추출(파싱)
soup = BeautifulSoup(response.content, 'lxml')
title_tags = soup.select('.tit-g a')

# 3단계: 결과 확인
for title_tag in title_tags:
    print(title_tag.text.strip())
    print(title_tag.get('href'))