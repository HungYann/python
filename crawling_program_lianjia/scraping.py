# coding:utf-8
import requests
from bs4 import BeautifulSoup
url = "https://www.163.com/"
data = requests.get(url).text
soup = BeautifulSoup(data,'lxml')
news_titles = soup.select("div>ul>li>a")

for n in news_titles:
    title = n.get_text()
    link = n.get('href')
    data = {
        '标题' : title,
        '链接' : link
    }
    print(data)
