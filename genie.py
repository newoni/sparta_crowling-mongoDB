'''
made by KH

request, bs4 활용한 크롤링
'''

import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

genie_url = 'https://www.genie.co.kr/chart/top200?ditc=D&ymd=20210119&hh=23&rtm=N&pg=1'

data = requests.get(genie_url, headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

#Using 'Copy selector'
table = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for row in table:
    rank = row.select_one('td.number').text.split('\n')[0]
    singer = row.select_one('td.info > a.artist.ellipsis').text
    name = row.select_one('td.info > a.title.ellipsis').text.strip()

    print(rank, name, singer, sep = '\t')

