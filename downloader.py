import requests
import time
from lxml import html
import webbrowser as web

def crawl():
    links=['https://class.coursera.org/ml-006/lecture']
    getmorelinks(links)
	

def getmorelinks(li):
    links=[]
    for i in range(0,len(li)):
        age = requests.get(li[i],stream=True)
        page=age.content
        
        x=li[i]+'/download.mp4'
        print x
        n=0
        c=page.count(x)
        print c
        while(n<c):
            index=page.find(x)
            index2=page.find('"',index+1)
            link=page[index:index2]
            links.append(link)
            n+=1
            page=page[index2+1:]
    
    maincrawl(links)


def maincrawl(links):
    for i in range(0,len(links)):
        web.open(links[i])
        time.sleep(10)


crawl()


