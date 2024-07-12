# install bs4 and lxml

from datetime import datetime
import requests
import csv
import bs4

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.3"
REQUEST_HEADER = {
    'USer-Agent': USER_AGENT,
    'Accept-Language': 'en-US, en;q=0.5',
}
def get_page_html(url):
    res = requests.get(url= url,headers=REQUEST_HEADER)
    return res.content

def get_product_price(soup):
    main_price_span = soup.find('span',attrs ={
        'class': 'a-size-mini olpWrapper'
    })   
    price = main_price_span.text.strip().split()
    list_len = len(price)
    final_price = price[list_len-1]     
    return final_price.replace('$','').replace(',','')

def get_product_title(soup):
    product_title = soup.find('span', id="productTitle" )
    return product_title.text.strip()
                              
def extract_product_info(url):
    product_info = {}
    print(f'Scraping URL: {url}')
    html = get_page_html(url = url)
    # print(html)
    soup = bs4.BeautifulSoup(html,'lxml')
    product_info['price'] = get_product_price(soup)
    product_info['title'] = get_product_title(soup)
    return product_info

if __name__ == "__main__":
    with open('amazon_products_url.csv',newline='') as csvfile:
        reader = csv.reader(csvfile,delimiter=',')
        for row in reader:
            url = row[0]
            # print(url)
            print(extract_product_info(url))

