# -*- coding: utf-8 -*-
"""
Created on Thu May 28 16:28:50 2020

@author: vincent.yu
"""
#해외센터 지역 코로나 현황 
#대상: 미국, 브라질, 러시아, 영국, 인도, 독일, 중국, 싱가폴, 베트남,한국
#데이터 출처 : 위키백과European Centre for Disease Prevention and Control

import os
os.environ["HTTP_PROXY"] = "http://70.10.15.10:8080"
os.environ["HTTPS_PROXY"] = "http://70.10.15.10:8080"
os.environ["PYTHONHTTPSVERIFY"] = "0"

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd


#from selenium import webdriver

#Today 
NOW = datetime.now() 
tYear = str(NOW.year) 
tMonth = str(NOW.month) 
if len(tMonth) == 1: 
    tMonth = '0'+tMonth 
 
 
tDay= str(NOW.day) 
if len(tDay) == 1: 
     tDay = '0'+tDay 
 
 
today = tYear+'-'+tMonth+'-'+tDay+' '+'한국시간.'
print(today)
print("\n")


#google base url 
base_url = "https://news.google.com/covid19/map?hl=ko&gl=KR&ceid=KR:ko"


resp = requests.get(base_url, verify = False)
html_src = resp.text
soup = BeautifulSoup(html_src,'html.parser')

#COVID-19 극가별 아이템 블럭을 선택
items = soup.select('tr[class="sgXwHf wdLSAe YvL7re"]') #전체 테이블 + 갯수 중요!!!
#print(items)
#print(len(items))

#target_countries=["미국", "브라질", "러시아", "영국", "인도", "독일", "중국", "싱가폴", "베트남"]


countries=[]; confirmeds=[]; confirmed_mills=[]; recovereds=[]; deaths=[];               
limit = 10 #top = 10
#index = 0
i = 0
for item in items[:limit]: # top=10
#for item in items:  
     # country = item.find('tr', {'class' :'sgXwHf wdLSAe YvL7re'}).text
     #country = item.find('div', {'class':'TWa0lb'}).text #국가, 전세계 포함
    country = item.find('div', {'class':'pcAJd'}).text #국가, 전세계 포함 
#    if country == "미국" :
#          countries.append(country)
#    else:
#           pass 
      #print(len(country))  
      #print(country)
    countries.append(country)
    #print(countries)
  
    #confirmed = item.find('td', {'class': 'l3HOY'}).text #숫자 1개  
    #print(confirmed)
    #confirmeds.append(confirmed)
    #print(countries, confirmeds)
    
    numbers = item.find_all('td')  #숫자 전부
    confirmed = numbers[0].text.strip()
    confirmeds.append(confirmed)
    
    confirmed_mill = numbers[1].text
    confirmed_mills.append(confirmed_mill)
    
    recovered   = numbers[2].text.strip()
    recovereds.append(recovered)
    
    death = numbers[3].text.strip()
    deaths.append(death)    
    
    #confirmed2 = confirmed2[0]
    #print(first,second,third, fourth)   
   
    
    #contents.append(content)
    
result = {'국가':countries,'확진자수':confirmeds,'백만명당':confirmed_mills, \
           '완치자수': recovereds,'사망자수': deaths}
df = pd.DataFrame(result, columns=['국가','확진자수' , '완치자수', '사망자수'])
df.to_excel("K:/My files/Download/google_covid19_reporting_06051640.xlsx")
print(df)
    
#news_reporting_date = news_reporting_datetime[0]
#news_reporting_time = news_reporting_datetime[1][:-1]
#reporting_dates.append(news_reporting_date)
#reporting_times.append(news_reporting_time)
