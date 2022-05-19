import requests
import bs4
res = requests.get('https://www.amazon.in')

soup =bs4.BeautifulSoup(res.text,'lxml')
links=soup.select('a')
img=soup.select('img')
print('number of links :'+str(len(links)))
print('number of images :'+str(len(img)))
