import requests
from bs4 import BeautifulSoup

url='https://news.ycombinator.com/'
response=requests.get(url)
soup=BeautifulSoup(response.text,'html.parser')

body=soup.body
#print(body)

find=soup.find(id='score_28231187')
#print(find)

# selectors for class is '.' and for id is '#'

s1=soup.select('.score')
#print(s1)

s2=soup.select('#score_28231187')
#print(s2)

votes=soup.select('.score')[3]
#print(votes)

links=soup.select('.storylink')[4]
#print(links)



