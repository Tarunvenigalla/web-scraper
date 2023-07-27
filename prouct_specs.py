from bs4 import BeautifulSoup
import requests

url=(input('Enter URL :'))
response=requests.get(url)
html=response.content
soup=BeautifulSoup(html,"html.parser")
brand=soup.find('tr',attrs={'class':'a-spacing-small po-brand'}).find('td',attrs={'class':'a-span9'}).text
model=soup.find('tr',attrs={'class':'a-spacing-small po-model_name'}).find('td',attrs={'class':'a-span9'}).text
screen_size=soup.find('tr',attrs={'class':'a-spacing-small po-display.size'}).find('td',attrs={'class':'a-span9'}).text
color=soup.find('tr',attrs={'class':'a-spacing-small po-color'}).find('td',attrs={'class':'a-span9'}).text
hard_disk=soup.find('tr',attrs={'class':'a-spacing-small po-hard_disk.size'}).find('td',attrs={'class':'a-span9'}).text
cpu_model=soup.find('tr',attrs={'class':'a-spacing-small po-cpu_model.family'}).find('td',attrs={'class':'a-span9'}).text
ram=soup.find('tr',attrs={'class':'a-spacing-small po-ram_memory.installed_size'}).find('td',attrs={'class':'a-span9'}).text
os=soup.find('tr',attrs={'class':'a-spacing-small po-operating_system'}).find('td',attrs={'class':'a-span9'}).text
price=soup.find('span',attrs={'class':'a-offscreen'}).text
print('Brand :',brand)
print('Model Name :',model)
print('Screen Size :',screen_size)
print('Color :',color)
print('Hard Disk :',hard_disk)
print('CPU Model :',cpu_model)
print('RAM Size :',ram)
print('Operating System :',os)
print('Price :',price)