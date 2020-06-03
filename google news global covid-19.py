import os

import requests
from bs4 import BeautifulSoup

import pandas as pd

#구글 뉴스 검색  
base_url = "https://news.google.com"
#base_url = "https://news.google.com/topstories?hl=ko&gl=KR&ceid=KR:ko"
# robots.txt -> /search? disallow 

# 전세계 코로나 현황 검색 
search_url = base_url + "/search?q=%EC%A0%84%EC%84%B8%EA%B3%84%20%EC%BD%94%EB%A1%9C%EB%82%98%20%ED%98%84%ED%99%A9&hl=ko&gl=KR&ceid=KR%3Ako"

# 코로나 국가별 순위 
#search_url = base_url + "/search?q=%EC%BD%94%EB%A1%9C%EB%82%98%20%EA%B5%AD%EA%B0%80%EB%B3%84%20%EC%88%9C%EC%9C%84&hl=ko&gl=KR&ceid=KR%3Ako"
resp = requests.get(search_url, verify = False)
html_src = resp.text
soup = BeautifulSoup(html_src,'html.parser')

#뉴스 아이템블럭을 선택
news_items = soup.select('div[class="xrnccd"]')
print('뉴스아이템 갯수:', len(news_items))
print(news_items[0])
print("\n")

for item in news_items[:3]:
    link = item.find('a', attrs={'class':'VDXfz'}).get('href')
    news_link = search_url + link[1:]
    print(news_link)
    
    news_title = item.find('a', attrs={'class':'DY5T1d'}).getText()
    print(news_title)
    
    news_content = item.find('span', attrs={'class':'xBbh9'}).text
    print(news_content)
    
    news_agency = item.find('a', attrs={'class':'wEwyrc AVN2gc uQIVzc Sksgp'}).text
    print(news_agency)
    
    news_reporting = item.find('time', attrs={'class':'WW6dff uQIVzc Sksgp'})
    news_reporting_datetime = news_reporting.get('datetime').split('T')
    news_reporting_date = news_reporting_datetime[0]
    news_reporting_time = news_reporting_datetime[1][:-1]
    print(news_reporting_date, news_reporting_time)
    print("\n")
    
def google_news_clipping(url,limit=5):
        resp = requests.get(url, verify = False)
        html_src = resp.text
        soup = BeautifulSoup(html_src,'html.parser')
        news_items = soup.select('div[class="xrnccd"]')
        
        # links=[]; titles=[];contents=[];agencies=[]; news_reporting_dates=[]; news_reporting_times=[];
        links=[]; titles=[];contents=[];agencies=[]; news_reporting_dates=[]; news_reporting_times=[];
        for item in news_items[:limit]:
            link = item.find('a', attrs={'class':'VDXfz'}).get('href')
            news_link = search_url + link[1:]
            links.append(news_link)
    
            news_title = item.find('a', attrs={'class':'DY5T1d'}).getText()
            titles.append(news_title)
    
            news_content = item.find('span', attrs={'class':'xBbh9'}).text
            contents.append(news_content)
    
            news_agency = item.find('a', attrs={'class':'wEwyrc AVN2gc uQIVzc Sksgp'}).text
            agencies.append(news_agency)
    
            news_reporting = item.find('time', attrs={'class':'WW6dff uQIVzc Sksgp'})
            news_reporting_datetime = news_reporting.get('datetime').split('T')
            #news_reporting_datetimes.append(news_reporting_datetime)
            news_reporting_date = news_reporting_datetime[0]
            news_reporting_time = news_reporting_datetime[1][:-1]
            news_reporting_dates.append(news_reporting_date)
            news_reporting_times.append(news_reporting_time)
            print(news_reporting_date, news_reporting_time)
            print("\n")
        result = {'link':links,'title':titles,'contents':contents, 'agency':agencies, \
                  'date':news_reporting_dates, 'time':news_reporting_times}
        #df = pd.DataFrame(result, columns=['link','title'])
        #df = pd.DataFrame(result, columns=['title','contents','date'])
        df = pd.DataFrame(result, columns=['title','contents','date','time'])
        df.to_excel("K:/My files/Download/google_news_scrap.xlsx")
        return result
        
news = google_news_clipping(search_url,5)
print(news)

"""
참조 코드  
#items = soup.select('div > article > div > div > a')   

#titles = [] 
#links = []
#for item in items:
#    title = item.text
#    link = base_url + item.get('href')[1:]
#    titles.append(title)
#    links.append(link)    
#data = {'link':links, 'title': titles}
#df = pd.DataFrame(data, columns=['link','title'])
#df.to_excel("C:/Users/vincent.yu/Spyder projects/ypy100/google_news scrap.xlsx")
"""
