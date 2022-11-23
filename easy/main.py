import requests
from bs4 import BeautifulSoup
import csv
from time import sleep

def write_to_csv(data):
    with open('easy_parsing.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(data)

def get_html(url):
    responce = requests.get(url)
    print(f'Статус: {responce.status_code}')
    return responce.text

def get_all_pages(html):
    soup = BeautifulSoup(html,'lxml')
    pages = int(soup.find('span', class_ = 'vm-page-counter').text.split()[-1])
    return pages


def get_data(html):
    soup = BeautifulSoup(html,'lxml')
    data = soup.find('div', class_ = 'browse-view').find_all('div', class_= 'row')
    for i in data:
        title = i.find('span', class_= 'prouct_name').find('a').text
        price = i.find('span', class_= 'price').text
        image = 'https://enter.kg' + i.find('img').get('src')
        write_to_csv([title, price, image])
   



def main():
    with open('easy_parsing.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['title','price','img'])
    url = 'https://enter.kg/computers/noutbuki_bishkek'
    html = get_html(url)
    pages = get_all_pages(html)
    for i in range(1,pages+1):
        print(i)
        if i == 1:
            url = 'https://enter.kg/computers/noutbuki_bishkek'
        else:
            url = 'https://enter.kg/computers/noutbuki_bishkek' +f'/results,{(i-1)*100+1}-{(i-1)*100}'
        print(url)
        html = get_html(url)
        get_data(html)


while True:
    main()
    sleep(3600)