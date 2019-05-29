#!/usr/bin/env python
# coding: utf-8

# In[2]:


print("hello python !!!")


# In[4]:


# 학습한 내용입니다
"""
학습한 내용들
"""


# In[5]:


from bs4 import BeautifulSoup #html 문서에서 정보 읽기


# In[7]:


from urllib.request import urlopen #웹 주소에서 html 파일 읽기


# In[8]:


url = urlopen("https://movie.naver.com/movie/running/current.nhn")
#웹페이지의 HTML 파일 내용 읽기


# In[10]:


soup = BeautifulSoup(url, "lxml")


# In[12]:


#print(soup)


# In[13]:


wrap = soup.find("div", {"class":"lst_wrap"}) 
# 영화 내용 부분만 간추림


# In[15]:


#print(wrap)


# In[16]:


titles = wrap.find_all("dt", {"class":"tit"})
#영화 제목 부분만 추리기


# In[18]:


#print(titles)


# In[19]:


#영화 제목만 가져오기
title = [] #영화 제목 저장하는 변수
for t in titles:
    title.append(t.find("a").text)


# In[21]:


#print(title)


# In[22]:


import csv #csv 파일을 읽는 모듈


# In[28]:


with open("c:\Demo.csv", "r") as f:
    data = list(csv.reader(f))    
    #참여자 수(Count Participants) 평균 구하기
    i = data[0].index("COUNT PARTICIPANTS")
    print(i)


# In[29]:


import statistics as stat


# In[30]:


# 전체 데이터에서 참여자 수(Count Participants)가 있는 열만 추리기
"""
1. 전체데이터(data) 슬라이스하여([1:]) 첫번째 제목열을 뺀다.
2. for 문의 row로 한줄씩 읽는다.
3. 참여자 수가 있는 인덱스(1)으로 특정한 값(참여자 수)를  읽는다.(row[i])
4. 문자열 데이터를 숫자로 바꾼다(int(row[i]))
5. 데이터를 리스트에 넣는다,
6. 2~5번을 마지막까지 반복한다.
"""
lists = [int(row[i]) for row in data[1:]]


# In[32]:


#print(lists)


# In[33]:


result = stat.mean(lists)
print(result)


# In[ ]:




