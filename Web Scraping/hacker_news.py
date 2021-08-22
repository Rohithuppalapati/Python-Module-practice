import requests
from bs4 import BeautifulSoup
import pprint

# Url to check and scrap

url='https://news.ycombinator.com/'
response=requests.get(url)
if response.status_code == 200:
    soup=BeautifulSoup(response.text,'html.parser')
else:
    print('please check URL')

#scrapping links and votes using selectors

links=soup.select('.storylink')
subtext=soup.select('.subtext')


#function to  get custom hacker news feed of over 100 votes

def custom_hn(links,subtext):
    hn=[]
    for index,items in enumerate(links):
        title=items.getText()
        href=items.get('href',None)
        vote=subtext[index].select('.score')
        if len(vote):
            points=int(vote[0].getText().replace(' points',''))
            if points>99:
                hn.append({'title':title,'links':href,'votes':points})

# desecending order sorted
    return sorted(hn,key=lambda k:k['votes'],reverse=True)

pprint.pprint(custom_hn(links,subtext))



