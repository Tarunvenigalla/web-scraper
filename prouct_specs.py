from bs4 import BeautifulSoup
import requests

def product_scrap(url):
    try:
        response=requests.get(url)
        if response.status_code!=200:
            print(f'Error: Failed to fetch web page (status code:{response.status_code})')
            return None
        soup=BeautifulSoup(response.content,"html.parser")
        brand=soup.find('h1',class_='yhB1nd').find('span',class_='B_NuCI').text
        price=soup.find('div',class_='_25b18c').find('div',class_='_30jeq3 _16Jk6d').text
        rating=soup.find('div',class_='_3LWZlK').text
        print('Product Details:',brand)
        print('Product Price  :',price)
        print('Product Rating :',rating)
       
    except Exception as e:
        print(f'Error: {e}')
        return None

target=input('Enter URL:')
scrap=product_scrap(target)

            
            
            