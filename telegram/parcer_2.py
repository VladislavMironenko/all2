import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import time

def get_first_news_1():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }

    url = 'https://www.bbc.com/ukrainian'
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, 'lxml')

    novosti = soup.find_all('li', class_="ebmt73l0 bbc-lpu9rr e13i2e3d1")

    new_dict_test = {}
    for novost in novosti:
        try:
            novost_title = novost.find('a' , class_="focusIndicatorDisplayInlineBlock bbc-1mirykb ecljyjm0").text.strip()
            novost_url = f'https://www.bbc.com{novost.find("a")["href"]}'
            # novost_time_element = novost.find('time').get('datetime')
            # date_from_iso = datetime.fromisoformat(novost_time_element)
            # date_time = datetime.strftime(date_from_iso , '%Y-%m-%d %H:%M:%S')
            # novost_date_time = time.mktime(datetime.strptime(date_time , '%Y-%m-%d %H:%M:%S').timetuple())

        except Exception as e:
            continue
        new_dict_test[str(novost_url)] = {
            "novost_title": novost_title,
            "novost_url": novost_url
        }
    # with open('new_dict_1.json' , 'w') as fail:
    #     json.dump(new_dict_test , fail , indent=4 , ensure_ascii=False)
def check_new_update_1():
    with open('new_dict_1.json') as file:
        new_dict_test = json.load(file)
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }

    url = 'https://www.bbc.com/ukrainian'
    r = requests.get(url = url , headers=headers)

    soup = BeautifulSoup(r.text , 'lxml')

    novosti = soup.find_all('li',class_="ebmt73l0 bbc-lpu9rr e13i2e3d1")

    fresh_news={}
    for novost in novosti:
        novost_url = f'https://www.bbc.com{novost.find("a")["href"]}'
        # novost_time_element = novost.find('time').get('datetime')
        # date_from_iso = datetime.fromisoformat(novost_time_element)
        # date_time = datetime.strftime(date_from_iso, '%Y-%m-%d %H:%M:%S')
        # novost_date_time = time.mktime(datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S').timetuple())
        if novost_url in new_dict_test:
            continue
        else:
            novost_title = novost.find('a', class_="focusIndicatorDisplayInlineBlock bbc-1mirykb ecljyjm0").text.strip()


            new_dict_test[str(novost_url)] = {
                "novost_title": novost_title,
                "novost_url": novost_url
            }
            fresh_news[str(novost_url)] = {
                "novost_title": novost_title,
                "novost_url": novost_url
            }
    with open('new_dict_1.json' , 'w' ) as file:
        json.dump(new_dict_test , file , indent=4 , ensure_ascii=False)

    for k, v in new_dict_test.items():
        if len(k) >= 200:
            with open('new_dict_1.json', 'w') as file:
                json.dump(new_dict_test, file, indent=4, ensure_ascii=False)
    return fresh_news

def main():
    check_new_update_1()
    get_first_news_1()
if __name__=='__main__':
    main()