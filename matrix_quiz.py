import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select('#old_content > table > tbody > tr')


# finding movie "matrix"
for i in trs:
    if (i.select_one('td.title > div > a') is not None) and (i.select_one('td.title > div > a').text=='매트릭스'):
        matrix_point = i.select_one('td.point').text


# finding movie that has same point of "matrix"
movie_names = []
for i in trs:
    if (i.select_one('td.title > div > a') is not None) and (i.select_one('td.point').text == matrix_point):
        buff = i.select_one('td.title > div > a').text
        movie_names.append(buff)
        print(buff)

# changing matrix point
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# 바꾸기 - 예시
db.movies.update_one({'title':'매트릭스'},{'$set':{'point':'0'}})


## finiding movie point "matrix" from DB
target_point = db.movies.find_one({'title':'매트릭스'})['point']

## finding movies that have same point of 'matirx'
movie_l = list(db.movies.find({'point':'9.39'},{'_id':False}))