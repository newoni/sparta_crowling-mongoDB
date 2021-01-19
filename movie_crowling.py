'''
naver 크롤링 자료를 mongoDB에 추가
'''

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303'

data = requests.get(url, headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select('#old_content > table > tbody > tr')


for tr in trs:
    num = tr.select_one('td:nth-child(1) > img')
    title = tr.select_one('td.title > div > a')
    point = tr.select_one('td.point')

    if title is not None:
        doc = {
            'title': title.text, 'num':num['alt'], 'point':point.text
        }

        db.movies.insert_one(doc)