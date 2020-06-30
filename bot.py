import telebot
import json
import requests


def parservalute(valute):
    response = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
    data = json.loads(response.text)['Valute']
    return data[valute]['Value']


token = 'your_token'
bot = telebot.TeleBot(token)
currencies = ['USD', 'EUR', 'GBP']



# обработчик команды start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,
'''Данный бот показывает текущий курс валют к рублю.
Введите команду /currency для получения списка валют.''')


# Обработчик команды currency и создание кнопок
@bot.message_handler(commands=['currency'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    for name in currencies:
        keyboard.add(name)
    bot.send_message(message.chat.id, 'Выберите валюту:', reply_markup=keyboard)


# Вывод курса
@bot.message_handler(content_types=['text'])
def send_text(message):
    for name in currencies:
        if message.text == name:
            bot.send_message(message.chat.id,
                             f'Курс {name} на данный момент составляет: {parservalute(name)} RUB')
            break
    else:
        bot.send_message(message.chat.id, 'Данной монеты нет в списке')


bot.polling()

