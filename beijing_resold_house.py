#coding:utf-8
import requests
from bs4 import BeautifulSoup
import time

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0;Win64;x64;rv:58.0) Gecko/20100101 Firefox/58.0',

}
with open('data.txt','w',encoding='utf-8') as f:
    for i in range(1,6):
        url = 'http://beijing.anjuke.com/sale/p'+str(i)
        r = requests.get(url,headers=headers)
        soup = BeautifulSoup(r.text, 'lxml')
        house_list = soup.find_all('li',class_="list-item")
        for house in house_list:
            house_name = house.find('div', class_="house-title").a.text.strip()
            house_price = house.find('span',class_="unit-price").text.strip()
            room_num = house.find('div',class_="details-item").span.text
            area = house.find('div',class_="details-item").contents[3].text
            high = house.find('div',class_="details-item").contents[5].text
            build_year = house.find('div',class_="details-item").contents[7].text
            address = house.find('span', class_="comm-address").text.strip()
            f.write(house_name+"/"+house_price+"/"+area+ "/"+room_num+'/'+high+'/'+build_year+'/'+address+'\n')
        time.sleep(5)
