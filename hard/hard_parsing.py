import requests
from bs4 import BeautifulSoup
import csv
from time import sleep

def write_to_csv(data):
    with open('hard_parsing.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(data)

def get_html(url):
    responce = requests.get(url)
    print(f'Статус: {responce.status_code}')
    return responce.text

def get_data(html):
    soup = BeautifulSoup(html,'lxml')
    data = soup.find('div', class_ = 'Tag--articles').find_all('div', class_ = 'Tag--article')
    count = 0
    titles = []
    sources = []
    d = {1: titles, 2: sources}
    for i in data:
        title = i.find('div', class_= 'ArticleItem--data ArticleItem--data--withImage').find('a', class_ = 'ArticleItem--name').text.strip()
        source = i.find('a', class_ = 'ArticleItem--name').get('href')
        sources.append(source)
        titles.append(f'{count+1}. {title}\n')
        count += 1
        if count == 20:
            break
    return d
def main():
    # with open('hard_parsing.csv', 'w') as file:
    #     writer = csv.writer(file)
        # writer.writerow(['news_title','source'])
    url = 'https://kaktus.media/?lable=8&date=2022-11-23&order=time'
    html = get_html(url)
    return get_data(html)
    

main()
# while True:
#     main()
#     sleep(3600)