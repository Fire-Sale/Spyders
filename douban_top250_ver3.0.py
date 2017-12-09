import requests,re
from bs4 import BeautifulSoup

nameList=[]
scoreList=[]
directorList=[]
playList=[]
yearList=[]
countryList=[]
commentList=[]
criticList=[]

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
    return nameList,scoreList,directorList,playList,yearList,countryList,commentList,criticList
def main():
    f=open('douban_top_250.txt','w',encoding='utf-8')
    Crawl()
    for i in range(25):
        print('Rank:'+str(i+1),file=f)
        print('Name:'+nameList[i],file=f)
        print('Director:'+directorList[i],file=f)
        print('Play:'+playList[i],file=f)
        print('Year:'+yearList[i],file=f)
        print('Country:'+countryList[i],file=f)
        print('Comment:'+commentList[i],file=f)
        print('Critic:'+criticList[i],file=f)
        print('Score:'+scoreList[i],file=f)
        print('\n',file=f)
    f.close()
main()
