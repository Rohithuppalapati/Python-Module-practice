import requests
from bs4 import BeautifulSoup

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
        title=links[index].getText()
        href=links[index].get('href',None)
        vote=subtext[index].select('.score')
        if len(vote):
            points=int(vote[0].getText().replace(' points',''))
            hn.append({'title':title,'links':href,'votes':points})

    return hn


print(custom_hn(links,subtext))


