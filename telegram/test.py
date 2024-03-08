import asyncio
import json
import time

import requests
from bs4 import BeautifulSoup
# from aiogram import Bot , Dispatcher , executor , types
import telebot




token = '6167770624:AAFsFS4fHZS6JsWYsa4Q86NGP2RSgJfsmXE'
channel_id = '@ukrinfo123'
sleep = 30
bot = telebot.TeleBot(token)


while True:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }

    url = 'https://www.rbc.ua/ukr'
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, 'lxml')

    novosti = soup.find_all('div', class_="item")
    new_dict = {}
    for novost in novosti:
        novost_title = novost.find('a').text.strip()
        novost_url = novost.find('a')['href'].strip()
        novost_time_element = novost.find('span', class_='time')
        novost_time = novost_time_element.text.strip() if novost_time_element else ''

        novost_id = novost_url.split('/')[-1]
        novost_id = novost_url.split('-')[-1]
        novost_id = novost_id[:-5]
        # print(f'{novost_title} | {novost_url} ')

        new_dict[novost_id] = {
            "novost_title": novost_title,
            "novost_url": novost_url
        }

        for channel in channel_id:
            bot.send_message(channel , novost)
            time.sleep(sleep)








# def get_first_news():
#     headers = {
#         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
#     }
#
#     url = 'https://www.rbc.ua/ukr'
#     r = requests.get(url = url , headers=headers)
#
#     soup = BeautifulSoup(r.text , 'lxml')
#
#     novosti = soup.find_all('div' ,class_="item")
#     new_dict={}
#     for novost in novosti:
#         novost_title = novost.find('a').text.strip()
#         novost_url = novost.find('a')['href'].strip()
#         novost_time_element = novost.find('span' , class_='time')
#         novost_time = novost_time_element.text.strip() if novost_time_element else ''
#
#         novost_id = novost_url.split('/')[-1]
#         novost_id= novost_url.split('-')[-1]
#         novost_id= novost_id[:-5]
#         # print(f'{novost_title} | {novost_url} ')
#
#         new_dict[novost_id] = {
#             "novost_title": novost_title,
#             "novost_url": novost_url
#         }
#     return new_dict
#
#
#
# def check_new_update():
#     with open('new_dict.json') as file:
#         new_dict = json.load(file)
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
#     }
#
#     url = 'https://www.rbc.ua/ukr'
#     r = requests.get(url=url, headers=headers)
#
#     soup = BeautifulSoup(r.text, 'lxml')
#
#     novosti = soup.find_all('div', class_="item")
#
#
#     fresh_news={}
#     for novost in novosti:
#         novost_url = novost.find('a')['href'].strip()
#         novost_id = novost_url.split('/')[-1]
#         novost_id= novost_url.split('-')[-1]
#         novost_id= novost_id[:-5]
#         if novost_id in new_dict:
#             continue
#         else:
#             novost_title = novost.find('a').text.strip()
#             novost_time_element = novost.find('span', class_='time')
#             novost_time = novost_time_element.text.strip() if novost_time_element else ''
#
#
#             new_dict[novost_id] = {
#                 "novost_title": novost_title,
#                 "novost_url": novost_url
#             }
#             fresh_news[novost_id] = {
#                 "novost_title": novost_title,
#                 "novost_url": novost_url
#             }
#     with open('new_dict.json' , 'w' ) as file:
#         json.dump(new_dict , file , indent=4 , ensure_ascii=False)
#     with open('new_dict.json') as file:
#         b = json.load(file)
#         for k, v in b.items():
#             if len(k) >= 200:
#                 with open('new_dict.json', 'w') as file:
#                     json.dump(new_dict, file, indent=4, ensure_ascii=False)
#     return fresh_news
# def main():
#     check_new_update()
#     get_first_news()
# if __name__=='__main__':
#     main()