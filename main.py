import requests
import random
import telebot
from bs4 import BeautifulSoup as tld

URL = 'https://www.anekdot.ru/last/good/'
API_KEY = '8019781655:AAFiwtmjfQsFUumTm29wNgXSoZZeE4QeTug'
def parser(url):
    r = requests.get(url)
    soup = tld(r.text, 'html.parser')
    anekdots = soup.find_all('div', class_='text'  )
    return [c.text for c in anekdots]

list_of_joks = parser(URL)
random.shuffle(list_of_joks)

bot = telebot.TeleBot(API_KEY)
@bot.message_handler(commands=['начать'])

def hello(message):
    bot.send_message(message.chat.id,'Салют! Введите любую цифру, чтобы рассмеяться')

@bot.message_handler(content_types=['text'])
def jokes (message):
    if message.text.lower() in '0123456789':
        bot.send_message(message.chat.id, list_of_joks[0])
        del list_of_joks[0]
    else:
        bot.send_message(message.chat.id, 'Введите любую цифру, от 0 до 9')

bot.polling()



# clear_anekdots = [c.text for c in anekdots]
# print(clear_anekdots)
# print(r.status_code)
# print(r.text) # download code web page
# print(anekdots)
