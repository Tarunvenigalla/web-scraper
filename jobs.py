from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
driver=webdriver.chrome("/url/lib/chromium-browser/chromedriver")
products=[]
prices=[]
ratings=[]
driver.get("https://www.amazon.in/Acer-12-Cores-Processor-Graphics-A515-57G/dp/B0B5KTSVTG/?_encoding=UTF8&pd_rd_w=1Qejt&content-id=amzn1.sym.3eb9b406-82b6-4bfd-8f57-210ceede3a6b&pf_rd_p=3eb9b406-82b6-4bfd-8f57-210ceede3a6b&pf_rd_r=AWMXG96V46474RFFPMJ5&pd_rd_wg=ZqMqN&pd_rd_r=0adaa600-ae9e-4092-9999-83c85606ee9f&ref_=pd_gw_gcx_gw_per_1&th=1")
content=driver.page_source
soup=BeautifulSoup(content)
for a in soup.findAll('a',href=True,attrs={'class':'a-section a-spacing-none'}):
    name=a.find('div',attr={'class':'a-size-large product-title-word-break'})
    price=a.find('div', attrs={'class':'a-price-whole'})
    rating=a.find('div', attrs={'class':'a-size-base a-color-base'})
products.append(name.text)
prices.append(price.text)
ratings.append(rating.text) 
df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings}) 
df.to_csv('products.csv', index=False, encoding='utf-8')