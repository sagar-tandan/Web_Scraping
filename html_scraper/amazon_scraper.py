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

def get_product_ratings(soup):
    product_rating_div = soup.find('div', id='averageCustomerReviews')
    product_rating_section = product_rating_div.find('i',attrs={
        'class':'a-icon-star'
    })
    product_rating_span = product_rating_section.find('span',attrs={
        'class': 'a-icon-alt'
    })
    try:
        return (product_rating_span.text.strip().split()[0])
        
    except ValueError:
        return 'Something went wrong'
    

def get_product_technical_details(soup):
    details = {}
    technical_details_section = soup.find('div', id = 'prodDetails')
    data_table = technical_details_section.findAll('table', id= 'productDetails_techSpec_section_1')
    for table in data_table:
        table_rows = table.findAll('tr')
        for row in table_rows:
            row_key = row.find('th').text.strip()
            row_value = row.find('td').text.strip().replace('\u200e','')
            details[row_key] = row_value
    return details
    
                   
def extract_product_info(url):
    product_info = {}
    print(f'Scraping URL: {url}')
    html = get_page_html(url = url)
    # print(html)
    soup = bs4.BeautifulSoup(html,'lxml')
    product_info['price'] = get_product_price(soup)
    product_info['title'] = get_product_title(soup)
    product_info['rating'] =get_product_ratings(soup)
    product_info.update(get_product_technical_details(soup))
    return product_info

if __name__ == "__main__":
    product_data = []
    with open('amazon_products_url.csv',newline='') as csvfile:
        reader = csv.reader(csvfile,delimiter=',')
        for row in reader:
            url = row[0]
            # print(url)
            product_data.append(extract_product_info(url))
            # print(product_data)
    output_filename = 'output-{}.csv'.format(datetime.today().strftime("%m-%d-%Y"))
    with open(output_filename,'w') as outputfile:
        writer = csv.writer(outputfile)
        writer.writerow(product_data[0].keys())
        for product in product_data:
            writer.writerow(product.values())

