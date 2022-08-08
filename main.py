import imp
from urllib import response
from bs4 import BeautifulSoup
import requests
import time
import sys, os

application_path = os.path.dirname(sys.executable)

def find_houses():
    html_text = requests.get('https://www.daft.ie/sharing/carlow-town-carlow').text
    html_text2 = requests.get('https://www.daft.ie/sharing/carlow-town-carlow?from=20&pageSize=20').text
    soup = BeautifulSoup(html_text, 'lxml')
    soup2 = BeautifulSoup(html_text2, 'lxml')
    house_offer = soup.find('span', class_ = 'TitleBlock__StyledSpan-sc-1avkvav-5 fKAzIL')
    offers = soup.find_all('li', class_ ='SearchPage__Result-gg133s-2 djuMQD')
    offers2 = soup2.find_all('li', class_ ='SearchPage__Result-gg133s-2 djuMQD')

    for index, offer in enumerate (offers):
        price = offer.find('div', class_ = 'TitleBlock__Price-sc-1avkvav-4 hiFkJc').text
        house_address = offer.find('p', class_ = 'TitleBlock__Address-sc-1avkvav-8 dzihyY').text
        link = offer.find('a', href = True)
        with open(f'{application_path}/Houses/{price}.doc', 'w') as f: 
            f.write(f"Price Displayed: {price} \n")
            f.write(f"House Address: {house_address} \n")
            f.write(f"Link: https://www.daft.ie/{link['href']} \n")
            print(f'''
                Price Displayed: {price}
                House Address: {house_address}
                Link: https://www.daft.ie/{link['href']}
            ''')
    for index, offer in enumerate (offers2):
        price2 = offer.find('div', class_ = 'TitleBlock__Price-sc-1avkvav-4 hiFkJc').text
        house_address2 = offer.find('p', class_ = 'TitleBlock__Address-sc-1avkvav-8 dzihyY').text
        link2 = offer.find('a', href = True)
        with open(f'{application_path}/Houses/{price2}.doc', 'w') as f: 
            f.write(f"Price Displayed: {price2} \n")
            f.write(f"House Address: {house_address2} \n")
            f.write(f"Link: https://www.daft.ie/{link2['href']} \n")
            print(f'''
                Price Displayed: {price2}
                House Address: {house_address2}
                Link: https://www.daft.ie/{link2['href']}
            ''')
if __name__ == '__main__': 
    while True: 
        find_houses()
        time_wait = 1
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)
   