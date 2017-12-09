import re
import requests
from bs4 import BeautifulSoup

def get_url(root_url,start):
    return root_url+"?start="+str(start)+"&filter="

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
        #temp=tag.find('p').get_text()
        dict['cast']=str(re.search(re.compile('导演: ...', re.S),tag.find('p').get_text()).group()).lstrip('导演: ').rstrip('·')
        dict['time']=str(re.search(re.compile('\d\d\d\d', re.S),tag.find('p').get_text()).group())
        '''if(re.search(re.compile('.国', re.S),tag.find('p').get_text())):
            dict['nation']=str(re.search(re.compile('.国', re.S),tag.find('p').get_text()).group())
        else:
            dict['nation']='error'''''
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
            print('Cast:'+movie.get('cast','No cast'),file=f)
            print('Description:'+movie.get('desc','No description'),file=f)
            #print('Nation:'+movie.get('nation'),file=f)
            print('Time:'+movie.get('time','No description'),file=f)
            print('\n',file=f)
        start+=25
    f.close()
main()
