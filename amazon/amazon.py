import csv
import requests
import json
from bs4 import BeautifulSoup as bs

def scrapAmazon(url, category):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
    req = requests.get(url, headers=headers)
    products = soup.findAll('div', {"class": "a-section a-spacing-none aok-relative"})
    items = []
    for product in products:
        # product number
        product_number = int(str(product.div.span.span.string)[1:])
        # product name and image
        image = product.find('img')
        image_url = image["src"]
        product_name = image['alt']
        # product ratting and price
        
        try:
            product_ratting_price = product.find('div', {"class":"a-icon-row"})
            product_price = float(re.findall(r'\d+.\d{2}', str(product.find('span', {'class': 'p13n-sc-price'}).string).replace(',', ''))[0])
        except:
            product_price = 0
            
        try:
            ratting_ratting = product_ratting_price.find('a').i.span.string
            product_ratting = float(re.findall('\d{1}.\d{1}', ratting_ratting)[0])
        except:
            product_ratting = 2.5
        # prodcuct seller

        try:
            product_seller = str(product.find('a', {'class': 'a-size-small a-link-child'}).text)
        except Exception as e:
            product_seller = "Unknown"

        product_seller
        item = {
            "description": product_name,
            "image": image_url,
            "number":product_number,
            "seller":product_seller,
            "price": product_price,
            "ratting": product_ratting,
            "category": str(category).upper()
        }
        items.append(item)
        
    ## WRITE TO A JSON FILE
    file = open(f'files/amazon_{category.lower()}.json', 'w')
    file.write(json.dumps(items))
    file.close()
    ## WRITTING TO A CSV FILE
    keys = items[0].keys()
    with open(f'files/amazon_{category.lower()}.csv', 'w', newline='')  as file:
        dict_writer = csv.DictWriter(file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(items)

    print("FILES SAVED!!", category)


amazon = "https://www.amazon.in/gp/bestsellers/software/ref=zg_bs_pg_2?ie=UTF8&pg=2"
category = "SOFTWARES"
scrapAmazon(amazon, category)

