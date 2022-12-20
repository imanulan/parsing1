import requests
from bs4 import BeautifulSoup as BS
import csv

def get_html(url):
    response = requests.get(url)
    return response.text

def get_soup(html):
    soup = BS(html,'lxml')
    return soup

def get_laptops(soup):
    laptops = soup.find_all('div',class_='ty-column4')
    
    for laptop in laptops:   
        try:
            title = laptop.find('a',class_='product-title').text.strip()
        except AttributeError:
            title = 'ноут?'
        try:
            price = laptop.find('span',class_='ty-price-num').text.strip()
        except AttributeError:
            price = '0'
        try:
            image = laptop.find('img',class_='ty-pict').get('data-ssrc')
        except AttributeError:
            image = ''

        write_csv({
            'title': title,
            'price': price,
            'image': image
        })    

def write_csv(data):
    with open('laptops.csv','a') as file:
        names = ['title','price','image']
        write = csv.DictWriter(file,delimiter=',',fieldnames=names)
        write.writerow(data)

def main():
    for i in range(1,79):        
        url = f'https://svetofor.info/noutbuki-planshety-bukridery/page-{i}'

        html = get_html(url)
        soup = get_soup(html)
        get_laptops(soup)
        print(f'спарсили {i} страницу')
if __name__ == '__main__':
    main()        