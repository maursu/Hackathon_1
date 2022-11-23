import requests
from bs4 import BeautifulSoup
import csv

def write_to_csv(data):
    with open('medium_parsing.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(data)

def get_html(url):
    response = requests.get(url)
    print(response.status_code)
    return response.text

def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    pages = int(soup.find('ul', class_ = 'pagination').find_all('li')[-1].find('a').get('data-page'))
    return pages

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    data = soup.find('div', class_ = 'search-results-table').find_all('div', class_ = 'list-item list-label')
    for i in data:
        title = i.find('h2', class_='name').text.strip()
        price = i.find('div', class_='block price').find('strong').text
        try:
            img = i.find('img').get('data-src')
        except:
            img = ''
        description = ' '.join(i.find('div', class_ = 'block info-wrapper item-info-wrapper').text.split())
        write_to_csv([title,price,img,description])


def main():
    with open('medium_parsing.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['title','price','img', 'description'])
    url = 'https://www.mashina.kg/search/all/'
    html = get_html(url)
    get_data(html)
    pages = get_total_pages(html)
    
    for i in range(1,pages+1):
        print(i)
        new_url = url +'?page=' + str(i)
        print(new_url)
        html = get_html(new_url)
        get_data(html)


main()