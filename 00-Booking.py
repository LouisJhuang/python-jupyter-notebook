#!/usr/bin/env python
# coding: utf-8

# In[ ]:




!conda install urllib3
# In[1]:


import requests
from bs4 import BeautifulSoup
#import lxml
#import urllib
#import re


# In[2]:


# 這個網頁必須是這樣 以下兩個個網址在此不能用(是給web browser用的!!)
web = "http://www.booking.com/hotel/tw/richardson.zh-tw.html?aid=304142;label=gen173nr-1FEghlcnJvcjQwNCiCAkICWFhIM2IFbm9yZWZo5wGIAQGYATC4AQbIAQzYAQHoAQH4AQuoAgM;sid=90b9c00bb8c3b7852742d43f6165a9c4;dcid=12;checkin=2016-03-28;checkout=2016-03-29;dest_id=-2637882;dest_type=city;dist=0;highlighted_blocks=132412401_85683812_0_0;room1=A%2CA;sb_price_type=total;srfid=e4cc12616d37bc46a3986294c48e495e1250c468X1;type=total;ucfs=1&lang=zh-tw#tab-reviews"

# 以下兩個個網址是給web browser用的!!

# 這是從F12 Network XHR Header中 得到的 網址
web = "https://www.booking.com/reviewlist.zh-tw.html?aid=304142;label=gen173nr-1FEghlcnJvcjQwNCiCAkICWFhIM2IFbm9yZWZo5wGIAQGYATC4AQbIAQzYAQHoAQH4AQuoAgM;sid=5359d7edc03f473e1747b8b55f54f8fb;cc1=tw;dist=1;pagename=richardson;r_lang=zh;roomtype=-1;type=total&;offset=20;rows=10&_=1516903624235"# 這是從selenium IDE中 按下下一頁按鈕 得到的 網址
web = "https://www.booking.com/reviewlist.zh-tw.html?aid=304142;label=gen173nr-1FEghlcnJvcjQwNCiCAkICWFhIM2IFbm9yZWZo5wGIAQGYATC4AQbIAQzYAQHoAQH4AQuoAgM;sid=5359d7edc03f473e1747b8b55f54f8fb;cc1=tw;dist=1;pagename=richardson;r_lang=zh;roomtype=-1;type=total&;offset=0;rows=10"
# In[ ]:





# In[3]:


res = requests.get(web)
#print res.text


# In[4]:


res

res.text
# In[ ]:





# In[5]:


soup = BeautifulSoup(res.text.encode("utf-8"),'lxml')


# In[ ]:





# In[6]:


soup.prettify()


# In[ ]:





# In[7]:


soup.find('div',{'class':'review_item_review_content'})


# In[8]:


soup.findAll('div',{'class':'review_item_review_content'})


# In[9]:


# 飯店整體的評分
soup.find_all("div",{"id":"review_list_score"})


# In[11]:


for string in soup.find_all("div",{"id":"review_list_score"}):
    #print(string.get_text("\n",strip=True))
    print(string.get_text(strip=True),"\n")


# In[ ]:





# In[12]:


#第一頁有幾位留言者之個別評分 不太有用!
soup.find_all('div',{'class':'review_item_header_score_container'})


# In[13]:


#第一頁有幾位留言者之個別評分 
hotel_score = soup.find_all('div',{'class':'review_item_header_score_container'})
for p in hotel_score:
    print(p.span.text.strip())


# In[ ]:





# In[14]:


#留言者姓名

hotel_lodger_name = soup.find_all('div',{'class':'review_item_reviewer' } ) 
for p in hotel_lodger_name:
    print(p.h4.text.strip())  #姓名為h4標籤   text部分只列印文字姓名 strip去頭尾空


# In[15]:


hotel_lodger_name = soup.find_all('div',{'class':'review_item_reviewer' } ) 
for p in hotel_lodger_name:
    print(p.h4.text.strip())  #姓名為h4標籤   text部分只列印文字姓名 strip去頭尾空白


# In[16]:


for news in soup.select('.review_item_reviewer'):
#找出所有 class:review_pos  的CSS
    #print(news)
    if(len(news.select('h4'))>0   ):
        print(news.select('h4')[0].text.strip())
        #h2 = (news.select('h4')[0].text.strip()) 


# In[ ]:





# In[ ]:





# In[17]:


soup.select('.review_item_review_content')


# In[18]:


soup.findAll('div',{'class':'review_item_review_content'})[0]


# In[19]:


soup.findAll('div',{'class':'review_item_review_content'})[0].findAll('p',{'class':'review_neg'})


# In[20]:


soup.findAll('div',{'class':'review_item_review_content'})[0].findAll('p',{'class':'review_pos'})


# In[21]:


soup.findAll('div',{'class':'review_item_review_content'})[0].findAll('p',{'class':'review_pos'})[0].get_text()


# In[22]:


for reviews in soup.findAll('div',{'class':'review_item_review_content'}):
    for review in reviews.findAll('p',{'class':'review_pos'}):
        print(review.get_text())


# In[23]:


for reviews in soup.findAll('div',{'class':'review_item_review_content'}):
    for review in reviews.findAll('p',{'class':'review_neg'}):
        print(review.get_text())


# In[ ]:





# In[ ]:





# In[24]:


soup.select('.review_item_review')


# In[25]:


soup.select('.review_item_review_content')


# In[ ]:





# In[26]:


for review in soup.select('.review_item_review_content'):        
    if(review.select('.review_neg')):
        print ("-:",review.select('.review_neg')[0].text)
    if (review.select('.review_pos')):
        print ("+:",review.select('.review_pos')[0].text)


# In[27]:


for review in soup.select('.review_item_review_content'):        
    if(review.select('.review_neg')):
        re = review.select('.review_neg')
        print ("-:", re[0].i.next_sibling)
        #print ("-:",review.select('.review_neg')[0].text)
    if (review.select('.review_pos')):
        #print ("+:",review.select('.review_pos')[0].text)
        print ("+:",review.select('.review_pos')[0].i.next_sibling)


# In[29]:


get_ipython().system('conda config --add channels conda-forge')
get_ipython().system('conda install selenium')

如何使用 Selenium 以及 Python 輕鬆抓取 Agoda 的旅館資訊?

https://www.youtube.com/watch?v=MQH4Rau_F_A# chrome driver如何使用請參考:
http://jialin128.pixnet.net/blog/post/114056630-%5Bpython%5D--%E4%BD%BF%E7%94%A8selenium%E5%9C%A8google-chrome%E7%80%8F%E8%A6%BD%E5%99%A8http://www.booking.com/hotel/tw/richardson.zh-tw.html?aid=304142;label=gen173nr-1FEghlcnJvcjQwNCiCAkICWFhIM2IFbm9yZWZo5wGIAQGYATC4AQbIAQzYAQHoAQH4AQuoAgM;sid=90b9c00bb8c3b7852742d43f6165a9c4;dcid=12;checkin=2016-03-28;checkout=2016-03-29;dest_id=-2637882;dest_type=city;highlighted_blocks=132412401_85683812_0_0;room1=A%2CA;sb_price_type=total;srfid=e4cc12616d37bc46a3986294c48e495e1250c468X1;type=total;ucfs=1&;lang=zh-tw#tab-reviewshttps://www.booking.com/reviewlist.zh-tw.html?aid=304142;label=gen173nr-1FEghlcnJvcjQwNCiCAkICWFhIM2IFbm9yZWZo5wGIAQGYATC4AQbIAQzYAQHoAQH4AQuoAgM;sid=5359d7edc03f473e1747b8b55f54f8fb;cc1=tw;dist=1;pagename=richardson;r_lang=zh;roomtype=-1;type=total&;offset=20;rows=10&_=1516903624235
# In[4]:


# 這是從F12 Network XHR Header中 得到的 網址
web = "https://www.booking.com/reviewlist.zh-tw.html?aid=304142;label=gen173nr-1FEghlcnJvcjQwNCiCAkICWFhIM2IFbm9yZWZo5wGIAQGYATC4AQbIAQzYAQHoAQH4AQuoAgM;sid=5359d7edc03f473e1747b8b55f54f8fb;cc1=tw;dist=1;pagename=richardson;r_lang=zh;roomtype=-1;type=total&;offset=20;rows=10&_=1516903624235"


# In[21]:


# 這是從selenium IDE中 按下下一頁按鈕 得到的 網址
web = "https://www.booking.com/reviewlist.zh-tw.html?aid=304142;label=gen173nr-1FEghlcnJvcjQwNCiCAkICWFhIM2IFbm9yZWZo5wGIAQGYATC4AQbIAQzYAQHoAQH4AQuoAgM;sid=5359d7edc03f473e1747b8b55f54f8fb;cc1=tw;dist=1;pagename=richardson;r_lang=zh;roomtype=-1;type=total&;offset=0;rows=10"


# In[97]:


from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
#browser = webdriver.Firefox(executable_path=r'./geckodriver.exe')
chrome_path = "./chromedriver.exe" #chromedriver.exe執行檔所存在的路徑
browser = webdriver.Chrome(chrome_path)
browser.get(web)
soup = BeautifulSoup(browser.page_source,"lxml")
count=0
limit_page=1
while len(soup.select('.page_link.review_next_page'))>0:
    for review in soup.select('.review_item_review'):        
        if(review.select('.review_neg')):
            print ("-:",review.select('.review_neg')[0].i.next_sibling)
        if (review.select('.review_pos')):
            print ("+:",review.select('.review_pos')[0].i.next_sibling)
    '''
    for reviews in soup.findAll('div',{'class':'review_item_review_content'}):
        for review in reviews.findAll('p',{'class':'review_pos'}):
            print('pos:',review.get_text())
    for reviews in soup.findAll('div',{'class':'review_item_review_content'}):
        for review in reviews.findAll('p',{'class':'review_neg'}):
            print('neg:',review.get_text())
    '''
    #for ele in soup.select('.review_item_review p'):
    #    print (ele.text[1:])
    browser.find_element_by_id("review_next_page_link").click()    
    soup = BeautifulSoup(browser.page_source,"lxml")
    print(count,'--------------------------')
    count=count+1
    if (count >= limit_page):
        break
    time.sleep(5)    
browser.close()


# In[ ]:




