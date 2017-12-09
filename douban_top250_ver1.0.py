import requests
from bs4 import BeautifulSoup

def get_url(root_url,start):
    return root_url+"?start="+str(start)

def scan(url):
    movies=[]
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"lxml")
    soup=soup.find('ol','grid_view')
    for tag in soup.find_all('li'):
        dict={}
        dict['rank']=tag.find('em').string
        dict['name']=tag.find('span','title').string
        dict['score']=tag.find('span','rating_num').string
        if(tag.find('span','inq')):
            dict['desc']=tag.find('span','inq').string
        dict['cast']=tag.find('p').get_text()
        movies.append(dict)
    return movies
def main():
    f=open('douban_top_250.txt','w',encoding='utf-8')
    root_url="https://movie.douban.com/top250"
    start=0
    while(start<250):
        movies=scan(get_url(root_url,start))
        for movie in movies:
            print('Rank:'+movie['rank'],file=f)
            print('Name:'+movie['name'],file=f)
            print('Score:'+movie['score'],file=f)
            print('Cast:'+movie['cast'],file=f)
            print('Description:'+movie.get('desc','No description'),file=f)
            print('\n',file=f)
        start+=25
    f.close()
main()
