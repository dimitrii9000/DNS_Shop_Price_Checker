
import requests
import telebot
from bs4 import BeautifulSoup as bs

# URL on item in the DNS shop
URL = 'https://www.dns-shop.ru/product/3a32483fb4cc3330/65-smartfon-apple-iphone-xs-max-64-gb-zolotistyj'

# Place there your prefered price
prefered_price = 80000

# Telegram bot token
bot = telebot.TeleBot('956905876:AAHqRP_A45LIldMQmDJZV8vu_XFuOpHjU3U')

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # HTML parser
    page = requests.get(URL, headers = headers)
    soup = bs(page.content, 'html.parser')
    title = soup.find(attrs={"data-product-param": "name"}).get_text()
    price = int(soup.find(attrs={"class": "current-price-value"}).get_text().replace(' ', ''))

    if price <= prefered_price:
        bot.send_message(message.from_user.id, "Цена на: {} упала до: {}".format(title, price))
    else:
        bot.send_message(message.from_user.id, ":( Цена все еще высока:  {}".format(price))


bot.polling(none_stop=True, interval=0)
