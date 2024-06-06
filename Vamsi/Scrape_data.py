import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

file_path = 'C:\\Users\\ravig\\OneDrive\\Desktop\\Python\\Python\\Vamsi\\new.html'
data=[]
with open(file_path, 'r', encoding='utf-8') as file:
    html = file.read()
soup=BeautifulSoup(html,'html.parser')
titels=soup.find_all('div',{'class':'KzDlHZ'})
print(titels)
prices=soup.find_all('div',{'class':'Nx9bqj _4b5DiR'})
print(prices)

length=min(len(titels),len(prices))
print(length)

for i in range(length):
    title=titels[i].get_text()
    price=float(prices[i].get_text().replace('₹','').replace(',',''))
    data.append({'title':title,'price':price})
print(data)

prices=[item['price'] for item in data]

plt.hist(prices,bins=10,edgecolor='black')
plt.show()
