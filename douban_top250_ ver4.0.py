import requests,re
from pandas import DataFrame
from bs4 import BeautifulSoup
from collections import Counter
import numpy as np

nameList=[]
scoreList=[]
directorList=[]
playList=[]
yearList=[]
countryList=[]
commentList=[]
criticList=[]
catagoryList=[]
cata=[]
countryt=[]
def Crawl():
    for page in range(10):
        url='https://movie.douban.com/top250?start='+str(page*25)
        html=requests.get(url)
        soup=BeautifulSoup(html.text,"lxml")
        soup=soup.find('ol','grid_view')
        for tag in soup.find_all('li'):
            contents=str(tag)
            name=re.compile(r'<span class="title">(.*?)</span>')
            names=re.findall(name,contents)
            for movieName in names:
                if(movieName.find('/')==-1):
                    nameList.append(movieName)

            score=re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>')
            scores=re.findall(score,contents)
            for movieScore in scores:
                scoreList.append(movieScore)

            director=re.compile(r'导演: (.*?) ')
            directors=re.findall(director,contents)
            for movieDirector in directors:
                directorList.append(movieDirector)

            play=re.compile('主演: (.*?)<br/>')
            plays=re.findall(play,contents)
            for moviePlay in plays:
                playList.append(moviePlay)
            if(plays==[]):
                playList.append('None')

            year=re.compile(r'(\d\d\d\d) / ')
            years=re.findall(year,contents)
            for movieyear in years:
                yearList.append(movieyear)

            country=re.compile(' / (.*?) / ')
            countries=re.findall(country,contents)
            for movieCountry in countries:
                countryList.append(movieCountry)
                temp=re.split(' ',movieCountry)
                for i in temp:
                    countryt.append(i)

            commentor=re.compile(r'<span>(.*?)人评价</span>')
            commentors=re.findall(commentor,contents)
            for movieCommentor in commentors:
                commentList.append(movieCommentor)

            critic=re.compile(r'<span class="inq">(.*?)</span>')
            critics=re.findall(critic,contents)
            for movieCritic in critics:
                criticList.append(movieCritic)
            if(critics==[]):
                criticList.append('None')

            catagory=re.compile(r'[(\d\d\d\d)] / (.*?) / (.*?)\n',re.S)
            catagorys=re.findall(catagory,contents)
            for movieCatagory in catagorys:
                catagoryList.append(movieCatagory[1])
                temp=re.split(' ',movieCatagory[1])
                for i in temp:
                    cata.append(i)
            if(catagorys==[]):
                catagoryList.append('Common')
    return nameList,scoreList,directorList,playList,yearList,countryList,commentList,criticList,catagoryList

def main():
    #f=open('douban_top_250_ver4.0.txt','w',encoding='utf-8')
    Crawl()
    data={'Name':nameList,'Director':directorList,'Play':playList,'Year':yearList,'Country':countryList,'Critic':criticList,'Score':scoreList,'Catagory':catagoryList}
    #DataFrame(data).to_csv('douban_top250.csv',index=False,encoding='utf_8_sig',columns=data.keys())

    print('Some conclusions:')
    print('Most common countries:')
    for k,v in dict(Counter(countryt).most_common(5)).items():
        print(k+':'+str(v))

    print('Most common years:')
    for k,v in dict(Counter(yearList).most_common(5)).items():
        print(k+':'+str(v))

    print('Most common catagories:')
    for k,v in dict(Counter(cata).most_common(5)).items():
        print(k+':'+str(v))
    #f.close()
main()
